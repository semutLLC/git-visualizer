# Git Visualizer

Visualizing how software communities evolve through recorded actions.

## Overview

Git Visualizer is an open-source project that analyzes Git repositories and transforms commit history into human-readable visualizations.

Every commit, review, and contribution leaves a trace. Over time, these traces accumulate into persistent memory, expertise, collaboration patterns, and project governance structures.

This project explores how higher-level coordination emerges from simple recorded actions.

## Goals

* Visualize commit history and contributor activity.
* Explore how expertise develops within projects.
* Identify collaboration patterns between contributors.
* Analyze long-term project evolution.
* Provide a foundation for broader coordination and knowledge-mapping systems.

## Initial Features

### Trace Layer

Raw activity recorded by Git:

* Commits
* Authors
* Timestamps
* Files changed

### Memory Layer

Aggregated history:

* Commit frequency
* Contributor timelines
* Repository growth
* Historical trends

### Knowledge Layer (Planned)

Inferred expertise:

* Directory ownership
* Subject matter specialization
* Knowledge concentration
* Knowledge transfer over time

## Example Questions

* Who contributes most frequently?
* Which areas of the codebase receive the most attention?
* How does expertise emerge?
* How does a project evolve over years?
* What patterns remain stable over time?

## Roadmap

### v0.1

* Parse Git history
* Count commits per contributor
* Generate activity charts

### v0.2

* Contributor network visualization
* File ownership analysis
* Repository evolution timeline

### v0.3

* Expertise inference
* Knowledge mapping
* Collaboration patterns

### v0.4

* Large-scale analysis of open-source projects
* Linux kernel visualization
* Cross-project comparisons

## Relation to the Semut Layer Model

Git Visualizer serves as an experimental implementation of concepts explored in the Semut Layer Model.

A Git repository can be viewed as:

* Trace → individual commits
* Memory → repository history
* Knowledge → accumulated expertise
* Norm → development practices
* Institution → project governance

The project focuses on making these layers observable through data and visualization.

## Status

Early prototype.

Contributions, feedback, and experimentation are welcome.
