import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info(phone_number_str, default_region="IN"):
    """
    Parses a phone number to find its registered country/region and carrier.
    Note: This DOES NOT track the real-time physical location of the device.
    """
    try:
        # Parse the phone number. Requires country code (e.g., +1, +44, +91)
        # We default to 'IN' (India) so you don't have to type +91 every time
        parsed_number = phonenumbers.parse(phone_number_str, default_region)
        
        # Check if it's a valid number format
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number."
            
        # Get the registered region (Country/State)
        region = geocoder.description_for_number(parsed_number, "en")
        
        # Get the carrier (network provider)
        provider = carrier.name_for_number(parsed_number, "en")
        
        return f"Registered Region: {region or 'Unknown'}\nCarrier: {provider or 'Unknown'}"
        
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Failed to parse the number. Ensure it includes the country code (e.g., +1 for US)."

if __name__ == "__main__":
    print("--- Phone Number Region Lookup ---")
    print("Note: This tool uses public numbering plan data to find where a number is registered.")
    print("It CANNOT track the real-time physical GPS location of a user.\n")
    
    user_input = input("Enter a phone number (with country code, e.g., +1234567890): ")
    print("\n--- Results ---")
    print(get_phone_info(user_input))
