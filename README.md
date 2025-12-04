# Rhythmic Ribbon MCP Server

MCP server providing visual vocabulary and aesthetic enhancement for rhythmic gymnastics ribbon dance compositions.

## Overview

Rhythmic gymnastics ribbon dance has a rich compositional structure spanning technical elements, spatial relationships, temporal dynamics, and expressive qualities. This server provides deterministic taxonomy mapping combined with LLM synthesis for cost-effective aesthetic enhancement.

## Architecture

**Three-Layer Olog Pattern:**

- **Layer 1**: Deterministic taxonomy mapping (ribbon elements, movements, spatial patterns)
- **Layer 2**: Structured parameter assembly (compositional rules, technical requirements)
- **Layer 3**: Single Claude synthesis call (aesthetic integration, expressive enhancement)

**Cost Savings**: ~60-80% compared to pure LLM approaches

## Features

### Tools
- `ribbon_enhance_prompt` - Enhance routine descriptions with technical and aesthetic vocabulary
- `ribbon_movement_vocabulary` - Get taxonomy of ribbon movement patterns
- `ribbon_spatial_vocabulary` - Explore spatial relationship categories
- `ribbon_temporal_vocabulary` - Access temporal dynamics and rhythm patterns
- `ribbon_composition_guide` - Get compositional structure guidance
- `ribbon_full_taxonomy` - Complete visual vocabulary taxonomy

### Technical Coverage
- **Movement Patterns**: Spirals, circles, snakes, figure-8s, throws, catches
- **Spatial Elements**: Height variations, planes, trajectories, distances
- **Temporal Dynamics**: Speed, rhythm, acceleration, transitions
- **Physical Properties**: Tension, arcs, waves, material behavior
- **Compositional Structure**: Sequences, coordination, musicality

## Installation

```bash
# From project root
pip install -e ".[dev]"

# Verify structure
./verify_structure.sh

# Run tests
./tests/run_tests.sh
```

## Usage

```python
from fastmcp import FastMCP

# The server provides ribbon dance visual vocabulary
# Use ribbon_enhance_prompt for aesthetic enhancement
# Access categorical taxonomies via vocabulary tools
```

## Quick Start

1. Install: `pip install -e ".[dev]"`
2. Verify: `./verify_structure.sh`
3. Test: `./tests/run_tests.sh`
4. Deploy: `fastmcp deploy`

## Documentation

See `docs/DOCUMENTATION.md` for complete API reference and examples.

## Pattern

This server follows the Standard MCP Server Setup Pattern:
1. Automated structure generation (`create_structure.sh`)
2. Manual large file placement (server.py, tests)
3. Structure verification (`verify_structure.sh`)
4. Package installation from root
5. Standard testing infrastructure

See `STRUCTURE_PATTERN.md` for reusable pattern details.
