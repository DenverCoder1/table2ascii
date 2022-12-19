## Contributing Guidelines

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a way to improve this project.

Make sure your request is meaningful and you have tested the app locally before submitting a pull request.

### Installing Requirements

#### Software Requirements

- [Python 3.7+](https://www.python.org/downloads/)

#### Development Dependencies

Install development dependencies with:

```bash
pip install -e ".[dev]"
```

Install documentation dependencies with:

```bash
pip install -e ".[docs]"
```

Install runtime dependencies with:

```bash
pip install -e .
```

All dependencies can be installed at once with:

```bash
pip install -e ".[dev,docs]"
```

### Running the Tests

Run the following command to run the [Tox](https://github.com/tox-dev/tox) test script which will verify that the tested functionality is still working.

```bash
task test
```

### Linting

Black, isort, and pre-commit hooks are used to lint the codebase. Run the following command to lint and fix the codebase.

```bash
task lint
```

### Pyright

To ensure that type hints are used correctly, Pyright is used to lint the codebase. Run the following command to check for typing errors.

```bash
task pyright
```

### Documentation

To view the documentation locally, run the following command.

```bash
task docs
```

The documentation will be served at <http://127.0.0.1:8888>.

### Need some help regarding the basics?

You can refer to the following articles on the basics of Git and GitHub in case you are stuck:

- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-an-issue-or-pull-request)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
- [Learn GitHub from Scratch](https://lab.github.com/githubtraining/introduction-to-github)