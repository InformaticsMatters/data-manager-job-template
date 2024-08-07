# data-manager-job-template

![Data Manager Job: 2021.1](https://img.shields.io/badge/data%20manager%20job-2021.1-000000?labelColor=dc332e)

```
FORK THIS REPOSITORY
AND REPLACE THE FOLLOWING
WITH YOUR OWN README/JOB DOCUMENTATION
```

![Architecture](https://img.shields.io/badge/architecture-amd64%20%7C%20arm64-lightgrey)

[![build](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/build.yaml/badge.svg)](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/build.yaml)
[![publish-tag](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/publish-tag.yaml/badge.svg)](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/publish-tag.yaml)
[![publish-stable](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/publish-stable.yaml/badge.svg)](https://github.com/InformaticsMatters/data-manager-job-template/actions/workflows/publish-stable.yaml)

![GitHub](https://img.shields.io/github/license/informaticsmatters/data-manager-job-template)

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/informaticsmatters/data-manager-job-template)

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

    poetry shell
    poetry install --no-root

    pre-commit install -t commit-msg -t pre-commit

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

1. `DEVELOPER-READEM.md` to name the repository you've forked to
2. `data-manager/manifest.yaml`
3. `data-manager/job.yaml`
4. The GitHub Actions, which expects repository secrets `DOCKERHUB_USERNAME`
   and `DOCKERHUB_TOKEN`
5. Adjust the `.gitignore` to satisfy your won tooling
6. Add tests (and test data)

## ARM64 (M1) processor support
To assist in local execution on the ARM64 (Apple M1) series of processors
your job container image must compile for its architecture. The GitHub actions
supplied in this template do that for you by employing the Docker [buildx]
actions.

You can test that your intended mage builds for the ARM64 processor using the
notes in this public [buildx gist].

---

[buildx]: https://docs.docker.com/buildx/working-with-buildx
[buildx gist]: https://gist.github.com/alanbchristie/14da3444f3fed6f0adcf877a82b56804.js
[im-jote]: https://pypi.org/project/im-jote
[use]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
