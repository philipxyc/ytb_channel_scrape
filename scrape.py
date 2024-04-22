import json
from ytb_search import YoutubeSearch
import time
import os

search_terms = [
    "Interior design tutorials", "Modern architecture", "Furniture design", "DIY home decor",
    "Product design", "Industrial design", "CAD for furniture", "3D printing in design",
    "Sustainable architecture", "Home renovation tips", "Landscape design", "Urban planning",
    "Virtual reality in architecture", "3D modeling for products", "Jewelry design in 3D",
    "Automotive design", "Aerospace modeling", "Toy design", "Fashion design technology",
    "Footwear design with 3D", "3D in textile manufacturing", "Custom furniture creation",
    "Eco-friendly building materials", "Smart home design", "Luxury goods design",
    "Packaging design innovation", "Sporting goods design", "3D visualizations for real estate",
    "Virtual property tours", "Animation in advertising", "Prototype modeling", "Cinematic set design",
    "Art installations", "Sculpture with 3D technology", "Educational models for schools",
    "Medical model visualization", "Biotech design", "Dental prosthetics 3D modeling",
    "Orthopedic implants in 3D", "3D mapping in geography", "Historical reconstructions",
    "Archaeological modeling", "Cultural heritage 3D scans", "Marine design and shipbuilding",
    "3D in consumer electronics", "Innovative kitchen tools", "3D modeling for carpentry",
    "Custom lighting design", "3D in musical instruments", "Event space design",
    "Stage design for performances", "Robotics and 3D modeling", "3D for gadget prototyping",
    "Augmented reality in design", "Mixed reality for training", "3D art exhibitions",
    "3D animations for education", "Interactive 3D learning tools", "3D puzzles and games",
    "Crafts and handmade design", "Theme park design", "Zoo exhibit design", "Aquarium structures",
    "Garden and patio design", "Outdoor sports facilities", "Recreational vehicle design",
    "Camping gear innovation", "Bicycle frame design", "Fitness equipment customization",
    "3D in military applications", "Emergency shelters in 3D", "Temporary structure design",
    "Portable building models", "3D in fashion shows", "Cosplay costumes design",
    "Virtual fashion and wearables", "3D in film and media", "Visual effects design",
    "User interface design in 3D", "Gaming accessories design", "Board game design with 3D",
    "Collectibles and figurines", "Model railway and dioramas"
]

search_termsv2 = [
    "Game development", "Indie game development", "Game design tutorials", "Unity 3D game development",
    "Unreal Engine tutorial", "Game programming", "Video game development", "Game development for beginners",
    "Mobile game development", "Game developer interview", "Blender 3D tutorials", "Maya 3D animation",
    "3D character modeling", "3D animation fundamentals", "Cinema 4D tutorials", "ZBrush sculpting tutorials",
    "3D texturing techniques", "Rigging for games", "Sculpting for game art", "3D model texturing",
    "AI in game design", "Neural networks for game AI", "Machine learning in games", "AI procedural generation",
    "AI for character behavior", "Deep learning for game developers", "AI in video games", "AI game programming",
    "AI-driven game testing", "AI for game balancing", "Game engine architecture", "Cross-platform game development",
    "VR game development", "AR game design", "Esports game creation", "Game physics programming",
    "Network programming for games", "Secure game development", "Game development tools", "Cloud services for gaming",
    "Blockchain in gaming", "NFTs in video games", "Game monetization strategies", "Game user experience design",
    "Player engagement strategies", "Game analytics", "Player retention techniques", "Esports tournament design",
    "Virtual goods in games", "Gaming community management"
]



# Load existing data if available
channels = {}
data_file = 'youtube_channels.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

# Main scraping function
def scrape_youtube():
    channels = load_data()
    total_channels_start = len(channels)
    for term in search_terms:
        print(f"Searching for term: {term}")
        results = YoutubeSearch(term, max_results=30).to_dict()
        for result in results:
            channel = result['channel']
            if channel not in channels:
                channels[channel] = {
                    'channel_name': result['channel'],
                    'channel': channel,
                    'videos': [],
                    'search_terms': []
                }
            if term not in channels[channel]['search_terms']:
                channels[channel]['search_terms'].append(term)
            channels[channel]['videos'].append({
                'title': result['title'],
                'video_id': result['id'],
                'views': result['views'],
                'publish_time': result['publish_time']
            })
        save_data(channels)
        print(f"Current number of unique channels: {len(channels)}")
        time.sleep(10)  # Sleep to prevent hitting the API limit quickly
    print(f"Total new channels added this session: {len(channels) - total_channels_start}")

if __name__ == '__main__':
    scrape_youtube()
