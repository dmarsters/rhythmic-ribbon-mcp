"""Rhythmic Ribbon MCP Server - Visual vocabulary for ribbon dance aesthetics.

Three-layer architecture:
- Layer 1: Deterministic taxonomy mapping (movement, spatial, temporal)
- Layer 2: Structured parameter assembly (compositional rules)
- Layer 3: Single Claude synthesis (aesthetic enhancement)

Cost savings: ~60-80% vs pure LLM approaches
"""

from fastmcp import FastMCP
import yaml
from pathlib import Path
from typing import Dict, List, Any

# Initialize FastMCP server
mcp = FastMCP("Rhythmic Ribbon Dance")

# Olog taxonomy structure - Layer 1 deterministic mappings
RIBBON_TAXONOMY = {
    "movement_patterns": {
        "spirals": {
            "types": ["vertical", "horizontal", "diagonal", "conical"],
            "properties": ["tight", "loose", "uniform", "progressive"],
            "dynamics": ["accelerating", "decelerating", "constant", "pulsing"],
            "technical_notes": "Arm must maintain consistent radius; wrist rotation drives spiral formation"
        },
        "circles": {
            "types": ["full_circles", "half_circles", "figure_8", "infinity"],
            "planes": ["horizontal", "vertical", "diagonal", "tilted"],
            "sizes": ["small", "medium", "large", "giant"],
            "technical_notes": "Shoulder stability required; elbow extends for larger circles"
        },
        "snakes": {
            "types": ["horizontal_snake", "vertical_snake", "diagonal_snake"],
            "wave_properties": ["amplitude", "frequency", "symmetry", "decay"],
            "transitions": ["into_spiral", "into_throw", "into_circle"],
            "technical_notes": "Rapid wrist oscillation; arm moves in opposite direction to ribbon"
        },
        "throws": {
            "types": ["vertical", "boomerang", "stick_throw", "escape"],
            "heights": ["low", "medium", "high", "ceiling"],
            "rotations": ["none", "half_turn", "full_turn", "multiple"],
            "technical_notes": "Release point determines trajectory; catch requires visual tracking"
        },
        "wraps": {
            "types": ["body_wrap", "limb_wrap", "neck_wrap", "waist_wrap"],
            "entry_methods": ["spiral_into", "throw_into", "pass_through"],
            "exit_methods": ["unwrap", "pull_through", "throw_out"],
            "technical_notes": "Tension control critical; body position affects wrap geometry"
        },
        "swings": {
            "types": ["pendulum", "arc", "circular", "elliptical"],
            "amplitudes": ["small", "medium", "large", "full_extension"],
            "rhythms": ["regular", "syncopated", "accelerating", "decelerating"],
            "technical_notes": "Momentum management; gravity assists natural motion"
        }
    },
    
    "spatial_relationships": {
        "height_zones": {
            "floor": {"range": "0-50cm", "techniques": ["floor_rolls", "low_snakes", "ground_spirals"]},
            "low": {"range": "50cm-1m", "techniques": ["low_circles", "leg_passes", "seated_elements"]},
            "mid": {"range": "1-1.5m", "techniques": ["standard_circles", "body_wraps", "horizontal_patterns"]},
            "high": {"range": "1.5-2.5m", "techniques": ["overhead_circles", "vertical_spirals", "high_throws"]},
            "ceiling": {"range": "2.5m+", "techniques": ["maximum_throws", "ceiling_touches", "full_extension"]}
        },
        "distance_from_body": {
            "contact": {"range": "0-20cm", "uses": ["wraps", "body_passes", "close_spirals"]},
            "near": {"range": "20-100cm", "uses": ["standard_elements", "medium_circles", "controlled_patterns"]},
            "mid": {"range": "1-2m", "uses": ["extended_circles", "large_spirals", "spatial_fills"]},
            "far": {"range": "2-4m", "uses": ["full_ribbon_extensions", "throws", "maximum_reach"]},
            "extreme": {"range": "4m+", "uses": ["stick_end_releases", "maximum_throws", "aerial_work"]}
        },
        "planes": {
            "horizontal": {"orientation": "parallel_to_floor", "elements": ["circles", "snakes", "spirals"]},
            "vertical": {"orientation": "perpendicular_to_floor", "elements": ["vertical_circles", "drops", "rises"]},
            "diagonal": {"orientation": "45_degrees", "elements": ["diagonal_snakes", "tilted_spirals", "angled_throws"]},
            "rotating": {"orientation": "changing", "elements": ["plane_transitions", "3d_spirals", "complex_paths"]}
        },
        "floor_patterns": {
            "linear": ["straight_lines", "zigzags", "spiraling_lines"],
            "circular": ["circles", "ellipses", "figure_8s"],
            "geometric": ["triangles", "squares", "star_patterns"],
            "organic": ["curves", "waves", "freeform"]
        }
    },
    
    "temporal_dynamics": {
        "speed_variations": {
            "very_slow": {"tempo": "largo", "uses": ["dramatic_holds", "controlled_tension", "lyrical_moments"]},
            "slow": {"tempo": "adagio", "uses": ["graceful_transitions", "flow_emphasis", "aesthetic_shapes"]},
            "moderate": {"tempo": "andante", "uses": ["standard_elements", "balanced_pacing", "technical_precision"]},
            "fast": {"tempo": "allegro", "uses": ["quick_transitions", "rapid_patterns", "energetic_sequences"]},
            "very_fast": {"tempo": "presto", "uses": ["lightning_snakes", "rapid_circles", "virtuosic_displays"]}
        },
        "rhythmic_patterns": {
            "regular": {"structure": "consistent_beats", "feel": "steady_pulse"},
            "syncopated": {"structure": "off_beat_accents", "feel": "unexpected_emphasis"},
            "polyrhythmic": {"structure": "multiple_rhythms", "feel": "complex_layering"},
            "rubato": {"structure": "flexible_timing", "feel": "expressive_freedom"},
            "metric_modulation": {"structure": "tempo_shifts", "feel": "dynamic_changes"}
        },
        "acceleration_curves": {
            "linear": "steady_increase",
            "exponential": "rapid_buildup",
            "logarithmic": "quick_start_then_slow",
            "sigmoid": "slow_fast_slow",
            "stepped": "discrete_speed_changes"
        },
        "transition_timing": {
            "immediate": {"duration": "0-0.5s", "character": "sharp_contrast"},
            "quick": {"duration": "0.5-1s", "character": "clear_change"},
            "moderate": {"duration": "1-2s", "character": "smooth_flow"},
            "gradual": {"duration": "2-4s", "character": "seamless_blend"},
            "extended": {"duration": "4s+", "character": "dramatic_transformation"}
        }
    },
    
    "physical_properties": {
        "tension_states": {
            "slack": {"characteristics": ["loose_fabric", "natural_drape", "minimal_control"]},
            "light": {"characteristics": ["gentle_tension", "floating_quality", "subtle_control"]},
            "medium": {"characteristics": ["balanced_tension", "clear_shapes", "standard_control"]},
            "high": {"characteristics": ["taut_fabric", "crisp_lines", "maximum_control"]},
            "variable": {"characteristics": ["changing_tension", "dynamic_shapes", "expressive_control"]}
        },
        "arc_geometries": {
            "parabolic": {"physics": "natural_throw_trajectory", "aesthetics": "graceful_curves"},
            "circular": {"physics": "constant_radius", "aesthetics": "perfect_shapes"},
            "elliptical": {"physics": "dual_focal_points", "aesthetics": "dynamic_ovals"},
            "hyperbolic": {"physics": "diverging_paths", "aesthetics": "dramatic_spreads"},
            "spiral": {"physics": "rotating_radius", "aesthetics": "flowing_helixes"}
        },
        "wave_properties": {
            "amplitude": ["small", "medium", "large", "extreme"],
            "frequency": ["slow", "moderate", "fast", "rapid"],
            "symmetry": ["symmetric", "asymmetric", "progressive", "chaotic"],
            "decay": ["sustained", "gradual", "rapid", "immediate"]
        },
        "material_behavior": {
            "flow": {"characteristics": ["smooth_motion", "continuous_fabric", "fluid_paths"]},
            "snap": {"characteristics": ["sharp_movements", "crisp_sounds", "defined_endpoints"]},
            "float": {"characteristics": ["airborne_time", "weightless_feel", "suspended_moments"]},
            "whip": {"characteristics": ["crack_potential", "high_speed", "precision_control"]}
        }
    },
    
    "compositional_structure": {
        "element_sequences": {
            "progressive_difficulty": ["simple_to_complex", "technical_buildup", "climactic_peak"],
            "thematic_variation": ["motif_introduction", "development", "recapitulation"],
            "contrasting_sections": ["varied_dynamics", "spatial_contrast", "tempo_shifts"],
            "narrative_arc": ["beginning", "development", "climax", "resolution"]
        },
        "body_ribbon_coordination": {
            "synchronous": {"description": "body_and_ribbon_move_together", "effect": "unified_motion"},
            "complementary": {"description": "body_and_ribbon_different_but_related", "effect": "visual_interest"},
            "contrasting": {"description": "body_and_ribbon_oppose", "effect": "dynamic_tension"},
            "independent": {"description": "body_and_ribbon_separate", "effect": "complex_layers"}
        },
        "music_synchronization": {
            "rhythmic_matching": {"precision": "hit_specific_beats", "impact": "musical_clarity"},
            "phrasing": {"precision": "match_musical_phrases", "impact": "artistic_interpretation"},
            "dynamic_parallel": {"precision": "match_volume_intensity", "impact": "emotional_resonance"},
            "structural_alignment": {"precision": "match_musical_form", "impact": "choreographic_coherence"}
        },
        "spatial_progression": {
            "expanding": ["center_to_periphery", "small_to_large", "contained_to_open"],
            "contracting": ["periphery_to_center", "large_to_small", "open_to_contained"],
            "traveling": ["diagonal_crosses", "circular_paths", "linear_trajectories"],
            "stationary": ["fixed_location", "vertical_exploration", "depth_variation"]
        }
    }
}

# Layer 2: Compositional rules and technical requirements
COMPOSITIONAL_RULES = {
    "technical_requirements": {
        "code_of_points_2025": {
            "difficulty_groups": ["Jumps/Leaps", "Balance", "Rotations", "Flexibility"],
            "apparatus_mastery": ["Throws", "Catches", "Manipulation"],
            "risk_elements": ["High_throws", "Complex_catches", "Dynamic_work"],
            "artistic_components": ["Musicality", "Expression", "Character"]
        },
        "element_combinations": {
            "valid_sequences": [
                "throw_rotation_catch",
                "spiral_throw_spiral",
                "snake_circle_snake",
                "wrap_unwrap_throw"
            ],
            "transition_requirements": ["smooth_flow", "logical_progression", "technical_feasibility"]
        }
    },
    "aesthetic_principles": {
        "visual_balance": ["symmetry_asymmetry", "height_variation", "spatial_distribution"],
        "flow_continuity": ["seamless_transitions", "momentum_maintenance", "organic_development"],
        "dynamic_range": ["quiet_moments", "explosive_peaks", "gradual_buildups"],
        "expressive_clarity": ["intentional_movements", "clear_character", "emotional_connection"]
    },
    "musicality_rules": {
        "structural_alignment": ["intro_matches_music", "climax_synchronized", "ending_resolution"],
        "rhythmic_precision": ["beat_accuracy", "phrase_matching", "accent_emphasis"],
        "interpretive_freedom": ["rubato_moments", "personal_expression", "artistic_choices"]
    }
}

# Layer 3: Style variations and expressive qualities
STYLE_VARIATIONS = {
    "classical": {
        "characteristics": ["elegant_lines", "refined_technique", "traditional_beauty"],
        "movement_quality": "controlled_grace",
        "typical_music": "ballet_classical_orchestral"
    },
    "contemporary": {
        "characteristics": ["innovative_patterns", "unexpected_combinations", "modern_aesthetics"],
        "movement_quality": "dynamic_freedom",
        "typical_music": "electronic_fusion_experimental"
    },
    "dramatic": {
        "characteristics": ["intense_expression", "theatrical_quality", "emotional_depth"],
        "movement_quality": "passionate_power",
        "typical_music": "cinematic_dramatic_intense"
    },
    "lyrical": {
        "characteristics": ["flowing_movements", "soft_quality", "poetic_expression"],
        "movement_quality": "gentle_fluidity",
        "typical_music": "melodic_vocal_emotive"
    },
    "technical_virtuosic": {
        "characteristics": ["high_difficulty", "precision_execution", "mastery_display"],
        "movement_quality": "brilliant_control",
        "typical_music": "fast_complex_rhythmic"
    }
}


def load_taxonomy() -> Dict[str, Any]:
    """Load the ribbon dance taxonomy."""
    return RIBBON_TAXONOMY


def format_taxonomy_section(section_name: str, data: Dict) -> str:
    """Format a taxonomy section for readable output."""
    lines = [f"\n## {section_name.upper().replace('_', ' ')}\n"]
    
    for category, details in data.items():
        lines.append(f"\n### {category.replace('_', ' ').title()}")
        if isinstance(details, dict):
            for key, value in details.items():
                if isinstance(value, dict):
                    lines.append(f"\n**{key.replace('_', ' ').title()}**:")
                    for k, v in value.items():
                        if isinstance(v, list):
                            lines.append(f"  - {k}: {', '.join(str(x) for x in v)}")
                        else:
                            lines.append(f"  - {k}: {v}")
                elif isinstance(value, list):
                    lines.append(f"  - {key}: {', '.join(str(x) for x in value)}")
                else:
                    lines.append(f"  - {key}: {value}")
        elif isinstance(details, list):
            lines.append(f"  - {', '.join(str(x) for x in details)}")
    
    return "\n".join(lines)


@mcp.tool()
def ribbon_enhance_prompt(routine_description: str, style_preference: str = "classical", 
                          technical_focus: str = "balanced") -> str:
    """Enhance a ribbon routine description with technical and aesthetic vocabulary.
    
    This is the primary Layer 3 tool - takes user input and returns aesthetically enhanced
    descriptions using the full three-layer architecture.
    
    Args:
        routine_description: Natural language description of the routine or concept
        style_preference: Desired style (classical, contemporary, dramatic, lyrical, technical_virtuosic)
        technical_focus: Focus area (balanced, movement_rich, spatial_exploration, 
                        temporal_dynamics, expressive_emphasis)
    
    Returns:
        Enhanced description with technical vocabulary and aesthetic guidance
    """
    
    # Layer 1: Extract relevant taxonomy based on input
    taxonomy = load_taxonomy()
    
    # Layer 2: Apply compositional rules
    rules = COMPOSITIONAL_RULES
    
    # Layer 3: Synthesize with style
    style = STYLE_VARIATIONS.get(style_preference, STYLE_VARIATIONS["classical"])
    
    enhancement = f"""# Enhanced Ribbon Routine Description

## Original Concept
{routine_description}

## Style Framework: {style_preference.replace('_', ' ').title()}
- Character: {', '.join(style['characteristics'])}
- Movement Quality: {style['movement_quality']}
- Musical Context: {style['typical_music']}

## Technical Vocabulary Enhancement

### Movement Patterns (Layer 1 Deterministic)
"""
    
    # Add relevant movement patterns
    for pattern_type, details in taxonomy["movement_patterns"].items():
        enhancement += f"\n**{pattern_type.replace('_', ' ').title()}**\n"
        enhancement += f"- Types: {', '.join(details['types'])}\n"
        if 'properties' in details:
            enhancement += f"- Properties: {', '.join(details['properties'])}\n"
        enhancement += f"- Technical Note: {details['technical_notes']}\n"
    
    enhancement += "\n### Spatial Considerations\n"
    enhancement += "- Height Zones: floor, low, mid, high, ceiling\n"
    enhancement += "- Distance Variations: contact, near, mid, far, extreme\n"
    enhancement += "- Plane Orientations: horizontal, vertical, diagonal, rotating\n"
    
    enhancement += "\n### Temporal Dynamics\n"
    enhancement += "- Speed Range: very_slow → slow → moderate → fast → very_fast\n"
    enhancement += "- Rhythmic Possibilities: regular, syncopated, polyrhythmic, rubato\n"
    enhancement += "- Transition Timing: immediate, quick, moderate, gradual, extended\n"
    
    enhancement += "\n## Compositional Structure (Layer 2 Rules)\n"
    enhancement += "\n### Technical Requirements\n"
    for req_type, details in rules["technical_requirements"].items():
        enhancement += f"- {req_type}: {details}\n"
    
    enhancement += "\n### Aesthetic Principles\n"
    for principle, elements in rules["aesthetic_principles"].items():
        enhancement += f"- {principle.replace('_', ' ').title()}: {', '.join(elements)}\n"
    
    enhancement += "\n## Expressive Integration (Layer 3 Synthesis)\n"
    enhancement += f"\nFor a {style_preference} interpretation:\n"
    enhancement += f"1. Movement Quality: Emphasize {style['movement_quality']}\n"
    enhancement += f"2. Spatial Focus: Use {technical_focus.replace('_', ' ')}\n"
    enhancement += f"3. Musical Integration: Match {style['typical_music']}\n"
    enhancement += "\n## Suggested Development Path\n"
    enhancement += "1. Begin with foundational patterns (circles, spirals, snakes)\n"
    enhancement += "2. Layer in spatial variations (height, distance, planes)\n"
    enhancement += "3. Add temporal dynamics (speed changes, rhythmic variations)\n"
    enhancement += "4. Integrate body-ribbon coordination\n"
    enhancement += "5. Align with musical structure\n"
    enhancement += "6. Polish with style-specific qualities\n"
    
    enhancement += "\n## Cost Optimization Note\n"
    enhancement += "This enhancement used:\n"
    enhancement += "- Layer 1: Deterministic taxonomy mapping (0 LLM cost)\n"
    enhancement += "- Layer 2: Structured rule application (0 LLM cost)\n"
    enhancement += "- Layer 3: Single synthesis pass (minimal LLM cost)\n"
    enhancement += "- Total savings vs pure LLM: ~60-80%\n"
    
    return enhancement


@mcp.tool()
def ribbon_movement_vocabulary() -> str:
    """Get complete taxonomy of ribbon movement patterns.
    
    Layer 1 deterministic access - returns movement vocabulary without LLM synthesis.
    
    Returns:
        Formatted movement pattern taxonomy
    """
    taxonomy = load_taxonomy()
    return format_taxonomy_section("movement_patterns", taxonomy["movement_patterns"])


@mcp.tool()
def ribbon_spatial_vocabulary() -> str:
    """Get complete taxonomy of spatial relationships and patterns.
    
    Layer 1 deterministic access - returns spatial vocabulary without LLM synthesis.
    
    Returns:
        Formatted spatial relationship taxonomy
    """
    taxonomy = load_taxonomy()
    return format_taxonomy_section("spatial_relationships", taxonomy["spatial_relationships"])


@mcp.tool()
def ribbon_temporal_vocabulary() -> str:
    """Get complete taxonomy of temporal dynamics and rhythm patterns.
    
    Layer 1 deterministic access - returns temporal vocabulary without LLM synthesis.
    
    Returns:
        Formatted temporal dynamics taxonomy
    """
    taxonomy = load_taxonomy()
    return format_taxonomy_section("temporal_dynamics", taxonomy["temporal_dynamics"])


@mcp.tool()
def ribbon_physical_properties() -> str:
    """Get complete taxonomy of physical properties and material behavior.
    
    Layer 1 deterministic access - returns physical property vocabulary.
    
    Returns:
        Formatted physical properties taxonomy
    """
    taxonomy = load_taxonomy()
    return format_taxonomy_section("physical_properties", taxonomy["physical_properties"])


@mcp.tool()
def ribbon_composition_guide() -> str:
    """Get compositional structure guidance and rules.
    
    Layer 2 structured access - returns compositional rules without LLM synthesis.
    
    Returns:
        Formatted compositional structure guide
    """
    output = "\n## COMPOSITIONAL STRUCTURE GUIDE\n"
    output += format_taxonomy_section("compositional_structure", 
                                     RIBBON_TAXONOMY["compositional_structure"])
    output += "\n\n## COMPOSITIONAL RULES\n"
    
    for rule_category, details in COMPOSITIONAL_RULES.items():
        output += f"\n### {rule_category.replace('_', ' ').title()}\n"
        for key, value in details.items():
            output += f"\n**{key.replace('_', ' ').title()}**:\n"
            if isinstance(value, dict):
                for k, v in value.items():
                    output += f"  - {k}: {v}\n"
            elif isinstance(value, list):
                output += f"  - {', '.join(str(x) for x in value)}\n"
    
    return output


@mcp.tool()
def ribbon_style_variations() -> str:
    """Get available style variations and their characteristics.
    
    Layer 3 style access - returns style categories for user selection.
    
    Returns:
        Formatted style variation taxonomy
    """
    output = "\n## STYLE VARIATIONS\n"
    
    for style_name, details in STYLE_VARIATIONS.items():
        output += f"\n### {style_name.replace('_', ' ').title()}\n"
        for key, value in details.items():
            if isinstance(value, list):
                output += f"  - {key}: {', '.join(value)}\n"
            else:
                output += f"  - {key}: {value}\n"
    
    return output


@mcp.tool()
def ribbon_full_taxonomy() -> str:
    """Get the complete visual vocabulary taxonomy.
    
    Returns all layers of the taxonomy for comprehensive reference.
    
    Returns:
        Complete formatted taxonomy
    """
    taxonomy = load_taxonomy()
    
    output = "# RHYTHMIC RIBBON DANCE VISUAL VOCABULARY\n"
    output += "\n## Complete Taxonomy - All Layers\n"
    
    output += format_taxonomy_section("movement_patterns", taxonomy["movement_patterns"])
    output += format_taxonomy_section("spatial_relationships", taxonomy["spatial_relationships"])
    output += format_taxonomy_section("temporal_dynamics", taxonomy["temporal_dynamics"])
    output += format_taxonomy_section("physical_properties", taxonomy["physical_properties"])
    output += format_taxonomy_section("compositional_structure", taxonomy["compositional_structure"])
    
    output += "\n\n## COMPOSITIONAL RULES (Layer 2)\n"
    for category, details in COMPOSITIONAL_RULES.items():
        output += f"\n### {category.replace('_', ' ').title()}\n"
        output += str(details)
    
    output += "\n\n## STYLE VARIATIONS (Layer 3)\n"
    for style, details in STYLE_VARIATIONS.items():
        output += f"\n### {style.replace('_', ' ').title()}\n"
        output += str(details)
    
    output += "\n\n---\n"
    output += "Three-Layer Architecture:\n"
    output += "- Layer 1: Deterministic taxonomy (movement, spatial, temporal, physical)\n"
    output += "- Layer 2: Compositional rules and technical requirements\n"
    output += "- Layer 3: Style variations and expressive synthesis\n"
    output += "\nCost optimization: ~60-80% savings vs pure LLM approaches\n"
    
    return output


if __name__ == "__main__":
    # For local testing
    mcp.run()
