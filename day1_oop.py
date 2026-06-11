class ModelConfiguration:
    def __init__(self, model_name):
        self.name = model_name
        # Initializing an empty dictionary to hold hyperparameter key-value pairs
        self.settings = {} 

    # Method to register or update a key-value setting
    def update_setting(self, key, value):
        self.settings[key] = value
        print(f"⚙️ Configured [{key}] -> {value}")

    # Method to read out all stored configurations
    def print_config(self):
        print(f"\n🛠️ --- {self.name} Parameters Summary ---")
        # Iterating over the dictionary items (keys and values together)
        for parameter, val in self.settings.items():
            print(f"🔹 {parameter}: {val}")
        print("Configuration matrix loaded successfully.\n")

# --- Running our Configuration Dictionary Object ---
# 1. Instantiate the configuration map
ai_config = ModelConfiguration("Learning_Base_v1")

# 2. Assigning key-value properties
ai_config.update_setting("learning_rate", 0.01)
ai_config.update_setting("epochs", 50)
ai_config.update_setting("optimizer", "Adam")

# 3. Printing our organized key-value layout
ai_config.print_config()