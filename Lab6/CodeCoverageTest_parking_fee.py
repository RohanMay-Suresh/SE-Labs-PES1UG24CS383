import pytest
from parking_fee import parking_fee, find_slot, monthly_pass


# parking_fee tests
def test_free_short_stay():
    assert parking_fee("car", 20, False, False) == 0


def test_unknown_vehicle():
    with pytest.raises(ValueError):
        parking_fee("bus", 60, False, False)


def test_negative_minutes():
    with pytest.raises(ValueError):
        parking_fee("car", -5, False, False)


def test_partial_hour_rounded_up():
    # 90 mins should be charged as 2 hours
    assert parking_fee("car", 90, False, False) == 60


def test_ev_half_price():
    assert parking_fee("bike", 90, True, False) == 10


def test_lost_ticket():
    assert parking_fee("car", 20, False, True) == 200


# find_slot tests
def test_full():
    assert find_slot("car", 0, False) == "full"


def test_disabled():
    assert find_slot("car", 5, True) == "ground floor"


def test_truck_basement():
    assert find_slot("truck", 5, False) == "basement"


def test_any_floor():
    assert find_slot("car", 5, False) == "any floor"


# monthly_pass tests
def test_bike_pass():
    assert monthly_pass("bike", False) == 500


def test_car_pass_resident():
    assert monthly_pass("car", True) == 1200


def test_no_pass_for_truck():
    with pytest.raises(ValueError):
        monthly_pass("truck", False)
