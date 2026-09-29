# Power-Factor-Calculator
import math

print("=" * 45)
print("       POWER FACTOR CALCULATOR")
print("=" * 45)

# Input values
voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))
real_power = float(input("Enter real power (W): "))

# Calculate apparent power
apparent_power = voltage * current

# Check input
if real_power <= 0:
    print("\nReal power must be greater than zero.")

elif real_power > apparent_power:
    print("\nError: Real power cannot be greater than apparent power.")

else:
    # Power factor
    power_factor = real_power / apparent_power

    # Reactive power
    reactive_power = math.sqrt(
        apparent_power**2 - real_power**2
    )

    # Phase angle
    phase_angle = math.degrees(
        math.acos(power_factor)
    )

    print("\n" + "=" * 45)
    print("              RESULTS")
    print("=" * 45)

    print(f"Voltage          : {voltage:.2f} V")
    print(f"Current          : {current:.2f} A")
    print(f"Real Power       : {real_power:.2f} W")
    print(f"Apparent Power   : {apparent_power:.2f} VA")
    print(f"Reactive Power   : {reactive_power:.2f} VAR")
    print(f"Power Factor     : {power_factor:.3f}")
    print(f"Phase Angle      : {phase_angle:.2f}°")

    # Power factor classification
    if power_factor >= 0.95:
        print("PF Status        : Good")

    elif power_factor >= 0.80:
        print("PF Status        : Moderate")

    else:
        print("PF Status        : Low")

    print("=" * 45)
