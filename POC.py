import time

def loading_animation():
    animations = ["Loading.", "Loading..", "Loading...", "Loading...."]
    for animation in animations:
        print(animation, end="\r")
        time.sleep(0.5)

def main():
    loading_animation()
    
    print("This code executes!")
    print("POC complete.")
if __name__ == "__main__":
    main()
