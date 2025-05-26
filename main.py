# Author: Alexandro Jauregui
import os
from utils.logger import setup_logger
from config_loader import load_config

# Initialize logger
logger = setup_logger("main")

# Load configuration
try:
    config = load_config()
    logger.info("Configuration loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load configuration: {e}")
    exit(1)

# Display loaded settings
logger.debug(f"Loaded config: {config}")


def main():
    logger.info("Audio Analysis Program Started")

    from audio_gen.signal_generator import generate_sine_wave
    from utils.audio_io import play_audio, record_audio, save_wav

    output_dir = "data/raw/"
    os.makedirs(output_dir, exist_ok=True)

    # Generate test tone
    signal = generate_sine_wave(
        freq=config["test_tone_freq"],
        duration=config["duration"],
        sample_rate=config["sample_rate"],
        amplitude=0.5
    )
    logger.info("Generated test sine wave.")

    # Play tone
    play_audio(signal, sample_rate=config["sample_rate"])
    logger.info("Playback complete.")

    # Record response
    recorded = record_audio(duration=config["duration"], sample_rate=config["sample_rate"])
    logger.info("Recording complete.")

    # Save both signals
    save_wav(os.path.join(output_dir, "generated_sine.wav"), signal, sample_rate=config["sample_rate"])
    save_wav(os.path.join(output_dir, "recorded_response.wav"), recorded, sample_rate=config["sample_rate"])
    logger.info("Saved both generated and recorded audio.")


if __name__ == "__main__":
    main()