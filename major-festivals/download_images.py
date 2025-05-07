import os
import requests
from PIL import Image
from io import BytesIO

def download_and_save_image(url, filename, size=(800, 600)):
    try:
        # Create images directory if it doesn't exist
        os.makedirs('static/images', exist_ok=True)
        
        # Set headers with User-Agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Download image
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Open and resize image
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')  # Convert to RGB mode
        img = img.resize(size, Image.Resampling.LANCZOS)
        
        # Save image
        filepath = os.path.join('static/images', filename)
        img.save(filepath, 'JPEG', quality=85)
        print(f"Successfully downloaded and saved: {filename}")
        
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Image URLs for each festival
images = {
    'diwali': {
        'main': 'https://www.picxy.com/photo/3075648',
        'intro': 'https://images.unsplash.com/photo-1605021303688-0a0c09425839',
        'significance': 'https://images.unsplash.com/photo-1605021302006-b5a3083c61f4',
        'celebration': 'https://images.unsplash.com/photo-1605021304066-fcb36e6f9a8e'
    },
    'holi': {
        'main': 'https://images.unsplash.com/photo-1576435728678-68d0fbf94e91',
        'intro': 'https://images.unsplash.com/photo-1581344895000-b86e1d2e5a1c',
        'legend': 'https://images.unsplash.com/photo-1581344946825-5e95c3aa6dc0',
        'celebration': 'https://images.unsplash.com/photo-1581344947724-6f8bf0f6f87f'
    },
    'harvest': {
        'main': 'https://images.unsplash.com/photo-1523348837708-15d4a09cfac2',
        'intro': 'https://images.unsplash.com/photo-1523348837708-15d4a09cfac3',
        'regional': 'https://images.unsplash.com/photo-1523348837708-15d4a09cfac4',
        'traditions': 'https://images.unsplash.com/photo-1523348837708-15d4a09cfac5'
    }
}

def main():
    # First, backup existing images
    backup_dir = 'static/images_backup'
    os.makedirs(backup_dir, exist_ok=True)
    
    # Move existing images to backup
    if os.path.exists('static/images'):
        for filename in os.listdir('static/images'):
            if filename.endswith('.jpg'):
                src = os.path.join('static/images', filename)
                dst = os.path.join(backup_dir, filename)
                try:
                    os.rename(src, dst)
                    print(f"Backed up {filename}")
                except Exception as e:
                    print(f"Error backing up {filename}: {str(e)}")

    # Download new images
    for festival, festival_images in images.items():
        for image_type, url in festival_images.items():
            filename = f"{festival}{'_' + image_type if image_type != 'main' else ''}.jpg"
            download_and_save_image(url, filename)

if __name__ == "__main__":
    main() 