# Developer README

## Building
The build takes place using GitHub Actions but a docker-compose file
is included to simplify local builds. To build the image run: -

    docker-compose build

## Testing
With the image built, use the Job tester utility: -

    python -m pip install --upgrade pip
    python -m pip install -r build-requirements.txt

And, from the project root, run the tester: -

    jote

---
