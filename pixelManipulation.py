from PIL import Image
import os
import random

def advanced_encrypt_image(input_image_path, output_image_path, key):
    """Encrypt an image using advanced pixel manipulation with modular arithmetic."""
    image = Image.open(input_image_path)
    pixels = image.load()

    # Image dimensions
    width, height = image.size
    random.seed(key)  # Initialize random seed with the key for consistency

    # Encrypt pixels
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Modular arithmetic ensures values stay in range [0, 255]
            r_enc = (r ^ key) % 256
            g_enc = (g ^ (key >> 1)) % 256
            b_enc = (b ^ (key >> 2)) % 256
            pixels[x, y] = (r_enc, g_enc, b_enc)

    # Shuffle rows for added complexity
    shuffled_rows = list(range(height))
    random.shuffle(shuffled_rows)
    new_image = Image.new("RGB", (width, height))
    for y, shuffled_y in enumerate(shuffled_rows):
        for x in range(width):
            new_image.putpixel((x, y), pixels[x, shuffled_y])

    # Save encrypted image
    new_image.save(output_image_path)
    print(f"Image encrypted and saved to: {output_image_path}")


def advanced_decrypt_image(input_image_path, output_image_path, key):
    """Decrypt an image by reversing the advanced encryption logic."""
    image = Image.open(input_image_path)
    pixels = image.load()

    # Image dimensions
    width, height = image.size
    random.seed(key)  # Initialize random seed with the key for consistency

    # Reverse row shuffling
    shuffled_rows = list(range(height))
    random.shuffle(shuffled_rows)
    unshuffled_image = Image.new("RGB", (width, height))
    for y, shuffled_y in enumerate(shuffled_rows):
        for x in range(width):
            unshuffled_image.putpixel((x, shuffled_y), pixels[x, y])

    unshuffled_pixels = unshuffled_image.load()

    # Decrypt pixels
    for x in range(width):
        for y in range(height):
            r, g, b = unshuffled_pixels[x, y]
            # Reverse encryption logic with modular arithmetic
            r_dec = (r ^ key) % 256
            g_dec = (g ^ (key >> 1)) % 256
            b_dec = (b ^ (key >> 2)) % 256
            unshuffled_pixels[x, y] = (r_dec, g_dec, b_dec)

    # Save decrypted image
    unshuffled_image.save(output_image_path)
    print(f"Image decrypted and saved to: {output_image_path}")


def main():
    print("\n=== Advanced Image Encryption & Decryption Tool ===")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    choice = input("Choose an option (1/2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return

    # Ask for input image path
    input_path = input("Enter the input image path: ").strip()

    if not os.path.isfile(input_path):
        print("Error: File not found. Please check the path.")
        return

    # Ask for encryption key
    try:
        key = int(input("Enter a key (integer value): ").strip())
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    # Set output paths
    output_path = input("Enter the output image path: ").strip()

    if choice == '1':
        advanced_encrypt_image(input_path, output_path, key)
    elif choice == '2':
        advanced_decrypt_image(input_path, output_path, key)


if __name__ == "__main__":
    main()
