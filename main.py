import pandas as pd

def recommend_outfit(user_input):
    # Load the outfits dataset
    outfits = pd.read_csv("outfits.csv")
    
    # Filter outfits based on user preferences
    outfit_recommendations = outfits[
        (outfits['Body_Type'].str.lower() == user_input['body_type'].lower()) &
        (outfits['Occasion'].str.lower() == user_input['occasion'].lower()) &
        (outfits['Mood'].str.lower() == user_input['mood'].lower()) &
        (outfits['Color_Palette'].str.lower() == user_input['color_palette'].lower())
    ]
    
    # Check if any outfit is found
    if outfit_recommendations.empty:
        return "Sorry, no matching outfits found. Try broadening your preferences!"
    else:
        # Return the first matching outfit
        return outfit_recommendations.iloc[0]['Outfit']

def main():
    print("👗 Welcome to StyleGPT – Your Virtual Stylist!")
    
    # Gather user preferences
    body_type = input("✨ What’s your body type? (Petite/Tall/Curvy/Athletic/Average): ").strip()
    occasion = input("🎉 What’s the occasion? (Casual/Party/Formal/Work/Travel): ").strip()
    mood = input("💖 What’s your mood today? (Bold/Minimal/Chic/Comfy/Playful): ").strip()
    color_palette = input("🎨 Favourite color palette? (Red/Black/Neutrals/Pastels/All): ").strip()
    
    # Store the preferences
    user_preferences = {
        'body_type': body_type,
        'occasion': occasion,
        'mood': mood,
        'color_palette': color_palette
    }
    
    # Get outfit recommendation
    outfit = recommend_outfit(user_preferences)
    
    print(f"🎉 Your recommended outfit is: {outfit}")

# Run the program
if __name__ == "__main__":
    main()
