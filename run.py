# run.py (Complete Code)
import argparse
import subprocess
import yaml
import os

def load_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def run_tests():
    parser = argparse.ArgumentParser(description="Automation Test Runner")
    parser.add_argument('--browser', default='chrome', help='Browser to run tests on.')
    parser.add_argument('--env', default='staging', help='Environment (staging or production).')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode.')
    args = parser.parse_args()

    # Load Configuration
    config = load_config('config/browser_config.yaml')
    base_url = config['environments'].get(args.env)
    
    # Build Pytest Environment Variables (passed to conftest.py)
    os.environ['TEST_BROWSER'] = args.browser
    os.environ['TEST_BASE_URL'] = base_url
    os.environ['TEST_HEADLESS'] = str(args.headless)

    pytest_command = ['pytest', 'tests/', '--verbose']

    print(f"\n--- Running tests on {args.browser.upper()} against {base_url} (Headless: {args.headless}) ---")

    # Execute Pytest
    try:
        subprocess.run(pytest_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Tests execution failed with error code: {e.returncode}")
    
if __name__ == '__main__':
    # Set the working directory to the project root for proper import resolution
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_tests()