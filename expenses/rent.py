from django.db.models import Count, Q

from vehicles.models import Vehicle, Passenger


def rent_calculate(id):
    vehicle = Vehicle.objects.get(id=id)
    rent = vehicle.monthly_rent
    passengers = vehicle.passengers.aggregate(
        oneside_count = Count('id', filter=Q(direction=Passenger.ONE_SIDE)),
        two_count=Count('id', filter=Q(direction=Passenger.BOTH_SIDE)),
        total=Count('id')
    )
    one_side_rent = rent / (passengers.oneside_count + (passengers.two_count * 2))
    return one_side_rent
