# python-gh-workflow

## Description

This repo provides examples of how to create basic workflows to automate common activities in a GitHub project. For example
code linting is a standard practice to enforce consistent code formatting and syntax. A linting task can be automated to run during
a particular stage of the develop process to insure code is properly linted prior to merging with existing functionality.

## GitHub workflow Hierarchy

A GitHub workflow is a YAML file in .github/workflows/ that defines when and how to run jobs. A GitHub action is a reusable unit of code that performs a specific task within a workflow.

Workflows orchestrate multiple actions and jobs, while actions are the individual building blocks that do the actual work.

A GitHub job is a group of steps that run on the same runner (virtual machine). Jobs contain multiple steps, and each step can use actions.

The hierarchy is: Workflow → Jobs → Steps → Actions

Jobs run in parallel by default, but can be configured to run sequentially with dependencies.
