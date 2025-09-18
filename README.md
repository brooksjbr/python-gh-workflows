# Python GitHub Workflows

## Description

This repo provides some examples of how to create workflows to automate common development activities in a GitHub project.
It's standard practice to format, lint, and test code prior to merging into a main branch. This is the primary way to maintain code quality and enforce particular coding standards. Automating these tasks using GitHub workflows reduces the burden of having to remember repetitive, but critical steps in an ever growing list of Todos expected of developers delivering features. These workflows can be applied in a variety of ways, this project will focus on the common scenario of creating a pull request for merging a feature into the main branch.

## Requirements and Configurations

Your GitHub account and repo will have to be configured to work in conjunction with the workflows, you need the following:

-   A GitHub account
-   GitHub account privleges allowing:
    -   Editing of account settings
    -   Installation of GitHub apps
    -   Creation of a repo under that account
    -   Editing the settings for that repo.
-   Python version >= 3.9
-   It is not required, but this project uses pyproject.toml and has a hard dependency for linting.

## Brief overview of GitHub Workflow Hierarchy

A GitHub workflow is a YAML file in .github/workflows/ that defines when and how to run jobs. A GitHub action is a reusable unit of code that performs a specific task within a workflow.

Workflows orchestrate multiple actions and jobs, while actions are the individual building blocks that do the actual work.

A GitHub job is a group of steps that run on the same runner (virtual machine). Jobs contain multiple steps, and each step can use actions.

The hierarchy is: Workflow → Jobs → Steps → Actions

Jobs run in parallel by default, but can be configured to run sequentially with dependencies.
