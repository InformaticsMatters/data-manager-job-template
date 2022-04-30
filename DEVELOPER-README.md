# Developer README

## Building
The build takes place using GitHub Actions. We would like to support
ARM64 (Apple M1) processors, so we use Docker's [buildx] to build the image: -

    docker buildx create --name mybuilder
    docker buildx use mybuilder
    docker buildx build . \
        --platform linux/amd64,linux/arm64 --output type=image \
        --tag informaticsmatters/data-manager-job-operator:latest

## Testing
With the image built, use the Job tester utility: -

    python -m pip install --upgrade pip
    python -m pip install -r build-requirements.txt

And, from the project root, run the tester: -

    jote

---

[buildx]: https://docs.docker.com/buildx/working-with-buildx
