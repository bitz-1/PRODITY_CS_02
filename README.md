# PRODITY_CS_02
pixel manipulation 


# Advanced Image Encryption & Decryption Tool

This tool allows you to encrypt and decrypt images using advanced pixel manipulation with modular arithmetic and row shuffling. It uses a key for both encryption and decryption processes to ensure the same transformation is applied in reverse during decryption.

## Features
- **Image Encryption**: Encrypt an image by applying advanced pixel manipulation and row shuffling.
- **Image Decryption**: Decrypt an image by reversing the encryption logic, restoring the original image.
- **Customizable Key**: Use any integer as the encryption/decryption key for added security.
- **Modular Arithmetic**: Ensures that pixel values stay within the valid RGB range (0–255).
- **Random Row Shuffling**: Adds an additional layer of complexity by shuffling rows during encryption and reversing the shuffle during decryption.

## Requirements
- Python 3.x
- Pillow (for image processing)

### Install the required library:

```bash
pip install pillow
```

## How to Use

1. **Clone or download the repository**:
    - Clone the repository or download the files to your local machine.

2. **Run the script**:
    - Open your terminal or command prompt and navigate to the directory containing the script.
    - Run the script with the following command:
    
    ```bash
    python image_encryption_tool.py
    ```

3. **Follow the on-screen prompts**:
    - When you run the script, you’ll be prompted to choose whether you want to **encrypt** or **decrypt** an image.
    - Enter the file path of the image you want to process.
    - Provide a custom **encryption key** (an integer value).
    - Specify the output file path where the processed image will be saved.

## Example Usage

### Encrypt an Image:
1. Choose option `1` to encrypt an image.
2. Provide the image file path (e.g., `input_image.jpg`).
3. Enter an encryption key, such as `12345`.
4. Provide the output file path (e.g., `encrypted_image.png`).

### Decrypt an Image:
1. Choose option `2` to decrypt an image.
2. Provide the encrypted image file path (e.g., `encrypted_image.png`).
3. Enter the decryption key (must match the encryption key used).
4. Provide the output file path for the decrypted image (e.g., `decrypted_image.jpg`).

## Code Walkthrough

### **Encryption (`advanced_encrypt_image`)**
- The function reads the image and processes each pixel by applying modular arithmetic (`(r ^ key) % 256`) for each color channel (red, green, blue).
- The rows of the image are shuffled randomly for added complexity, using the `random` library seeded with the provided key.

### **Decryption (`advanced_decrypt_image`)**
- The function reverses the encryption process by first undoing the row shuffling, then applying the reverse modular arithmetic to each color channel to retrieve the original pixel values.

## Example

### Encryption Example:
```bash
Enter the input image path: input_image.jpg
Enter a key (integer value): 12345
Enter the output image path: encrypted_image.png
Image encrypted and saved to: encrypted_image.png
```

### Decryption Example:
```bash
Enter the input image path: encrypted_image.png
Enter a key (integer value): 12345
Enter the output image path: decrypted_image.jpg
Image decrypted and saved to: decrypted_image.jpg
```

## Notes
- Ensure that you use the **same key** for both encryption and decryption.
- The tool works for images in **JPEG** or **PNG** format.
- Be cautious with key selection, as different keys will yield completely different encrypted results.

## License
This tool is released under the MIT License.
