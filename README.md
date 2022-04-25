# data-manager-job-template

![Data Manager Job: 2021.1](https://img.shields.io/badge/data%20manager%20job-2021.1-000000?labelColor=dc332e)

```
FORK THIS REPOSITORY
AND REPLACE THE FOLLOWING
WITH YOUR OWN README/JOB DOCUMENTATION
```

A GitHub Template Repository that you can [use] for Data Manager Job
implementations.

This repository is a minimal template for Data Manager Jobs. Although it contains
scaffolding to test and build a Python-based Job, including GitHub actions to
build and publish the implementation container image you can replace the
`src` files and associated `Dockerfile` to support any language you choose.
Ultimately the Job is published as a container image, you simply have to
provide the implementation and a suitable `data-manager/jobs.yaml`
definition.

From a fork you should be able to build and run the tests for the example
Job that it defines, start with this, and you'll know you're starting with
a working framework: -

    python -m venv venv
    source venv/bin/activate
    python -m pip install -r build-requirements.txt

    docker-compose build
    jote

    deactivate   

> Note: You MUST provide at least one test for every Job your repository
defines, and you MUST use our Job Tester ([im-jote]) to run those tests -
it's what we will use and if it fails the Job Tester we are unlikely
to deploy the image.

You must have at least one manifest file and at least one job definition file.
This template contains a single working example.

As well as replacing this README with your own you will want to
adjust the following additional files: -

1. The `docker-compose.yaml`, which creates an image using our image prefix
2. `data-manager/manifest.yaml`
3. `data-manager/job.yaml`
4. The GitHub Actions, which expects repository secrets `DOCKERHUB_USERNAME`
   and `DOCKERHUB_TOKEN`
5. Adjust the `.gitignore` to satisfy your won tooling
6. Add tests (and test data)

---

[im-jote]: https://pypi.org/project/im-jote
[use]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
