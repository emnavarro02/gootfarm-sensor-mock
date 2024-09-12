# CONTRIBUITING

Please refer to these contributing guidelines.

# Git commit message

Standardizing git commit messages enables: 

* Automating the CHANGELOG generation,
* More straightforward navigation through git history (e.g., ignoring style changes).
* Conventions may vary from project to project, so ensure you follow the pattern of the project you are working on.

# The 7 rules

Keep in mind these 7 rules for creating good git commit messages:

1. Separate the subject from the body with a blank line;
1. Limit the subject line to 50 characters;
1. Capitalize the subject line;
1. Do not end the subject line with a period;
1. Use the imperative mood in the subject line;
1. Wrap the body at 72 characters;
1. Use the body to explain what and why vs. how;

## Format of the commit message:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**Example**:
```
Feat(gui): Identify input message's intent

Use NLP to identify the message's intention and classify the message
greeetings, temperature, or humidity. Processing results are written
to the console

Refers to: #8
``` 

## Commit "type" verbs

* **build**: Build-related changes (for updating build configuration, development tools, or other changes irrelevant to the user);
* **chore**: A code change that the external user is not going to see (e.g., change to .gitignore file or .prettierrc file);
* **feat**: A new feature (relates to MINOR version);
* **fix**: A bug fix (relates to the PATCH version);
* **docs**: Documentation-related changes;
* **refactor**: A code that neither fixes a bug nor adds a feature. (e.g., you can use this when there are semantic changes like renaming a variable/ function name);
* **perf**: A code that improves performance (relates to the PATCH version);
* **style**: A code related to styling (i.e., formatting changes, missing semicolons, etc.);
* **test**: Adding new test or making changes to existing test;

### Scope values

The scope is an optional noun that represents a section of the codebase. If the scope is empty, the parentheses should be omitted. The following are scope examples:

* coordinator
* database
* gui
* sensor-node
* etc.

### Semantic Versioning 

Given a version number `MAJOR`.`MINOR`.`PATCH`, increment the:

* **MAJOR** version, when you make incompatible API changes;
* **MINOR** version, when you add functionality in a backward-compatible manner;
* **PATCH** version, when you make backward-compatible bug fixes;

--- 

## References:

* https://github.com/knowbl/git-commit-message
* https://dev.to/i5han3/git-commit-message-convention-that-you-can-follow-1709 
* https://semver.org/