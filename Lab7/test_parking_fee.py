from hypothesis import given, strategies as st
from parking_fee import minutes_parked, hourly_rate, format_plate

# Valid inputs, used to check that hardening did not break correct behaviour.
hours = st.integers(min_value=0, max_value=23)
mins = st.integers(min_value=0, max_value=59)
plate_letters = st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", min_size=2, max_size=2)
plate_digits = lambda n: st.text(alphabet="0123456789", min_size=n, max_size=n)


# minutes_parked
@given(st.text() | st.none())
def test_minutes_parked_no_crash(s):
    try:
        minutes_parked(s)
    except Exception as e:
        assert False, f"minutes_parked crashed with: {e!r}"

@given(st.from_regex(r"[0-9]{1,2}:[0-9]{2}-[0-9]{1,2}:[0-9]{2}", fullmatch=True))
def test_minutes_parked_never_negative(s):
    result = minutes_parked(s)
    assert result is None or result >= 0, f"negative duration {result} for {s!r}"

@given(hours, mins, hours, mins)
def test_minutes_parked_valid_times(h1, m1, h2, m2):
    start, end = h1 * 60 + m1, h2 * 60 + m2
    s = f"{h1:02d}:{m1:02d}-{h2:02d}:{m2:02d}"
    if end >= start:
        assert minutes_parked(s) == end - start
    else:
        assert minutes_parked(s) is None


# hourly_rate
@given(st.text() | st.none())
def test_hourly_rate_no_crash(s):
    try:
        hourly_rate(s)
    except Exception as e:
        assert False, f"hourly_rate crashed with: {e!r}"

@given(st.sampled_from(["bike", "car", "truck"]), st.sampled_from(["", " ", "  "]))
def test_hourly_rate_known_vehicles(vehicle, pad):
    expected = {"bike": 10, "car": 30, "truck": 60}[vehicle]
    assert hourly_rate(pad + vehicle.upper() + pad) == expected


# format_plate
@given(st.text() | st.none())
def test_format_plate_no_crash(s):
    try:
        format_plate(s)
    except Exception as e:
        assert False, f"format_plate crashed with: {e!r}"

@given(plate_letters, plate_digits(2), plate_letters, plate_digits(4))
def test_format_plate_valid(state, district, series, number):
    plate = state + district + series + number
    assert format_plate(plate) == f"{state.upper()} {district} {series.upper()} {number}"
