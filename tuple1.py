def format_itineraries(itineraries):
    result = []

    for i, (traveler_name, origin, destination) in enumerate(itineraries, start = 1):
        result.append(f"Itinerary{i}: {traveler_name} - from {origin} to {destination}")
    return "\n".join(result)

flight_itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

formatted_itineraries = format_itineraries(flight_itineraries)
print(formatted_itineraries)
