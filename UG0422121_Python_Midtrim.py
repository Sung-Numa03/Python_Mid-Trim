def _cylinder_properties(radius, height):
    """
    Calculates the area and volume of a cylinder.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        tuple: A tuple containing (area, volume).
    """
    import math

    # Calculate the area of the base (circle)
    base_area = math.pi * radius**2

    # Calculate the lateral surface area (rectangle)
    lateral_area = 2 * math.pi * radius * height

    # Calculate the total surface area
    total_area = 2 * base_area + lateral_area

    # Calculate the volume
    volume = base_area * height

    return total_area, volume

radius_input = float(input("Enter the radius of the cylinder: "))
height_input = float(input("Enter the height of the cylinder: "))

area, volume = _cylinder_properties(radius_input, height_input)
print(f"Total Surface Area: {area:.2f} square units")
print(f"Volume: {volume:.2f} cubic units")