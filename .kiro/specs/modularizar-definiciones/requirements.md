# Requirements Document

## Introduction

This document specifies the requirements for modularizing the monolithic `00_definiciones.rpy` file in "The Fifth Choice" visual novel project. The current 600-line file contains all game definitions (characters, variables, assets, logic) and has become difficult to maintain as the project grows.

The modularization will separate these definitions into 12 specialized modules with clear responsibilities, improving maintainability, reducing merge conflicts, and enabling parallel development. The refactoring must preserve all functionality and maintain backward compatibility with existing chapters and save files.

**Project Context**: Ren'Py 8.5.3 visual novel with 5 romantic routes, hidden affinity system, and multiple chapters.

**Goals**:
- Improve developer productivity (3-5x faster to find and modify definitions)
- Reduce merge conflicts (80% reduction in conflict scope)
- Enable scalable growth (prepare for 5x content increase in future chapters)
- Maintain 100% backward compatibility with existing code and saves

**Scope**: This refactoring affects only the core definitions file. Narrative chapters (01_, 02_, etc.) remain unchanged.

---

## Requirements

### 1. Functional Requirements

### 1.1 Modular Architecture

**Priority**: P0 (Critical)

The system shall decompose the monolithic `00_definiciones.rpy` file into 12 specialized modules with clear responsibilities.

**Acceptance Criteria**:
- Each module has a single, well-defined responsibility
- Module names follow the pattern `00[a-z]_*.rpy` or `00[a-z][0-9]_*.rpy`
- The dependency graph is acyclic (no circular dependencies)
- All modules compile successfully with `renpy.lint()`

**Rationale**: A monolithic 600-line file is difficult to maintain, causes merge conflicts, and slows development. Modularization improves code organization and team collaboration.

---

### 1.2 Dependency Management

**Priority**: P0 (Critical)

The system shall ensure that all module dependencies are loaded in the correct order using Ren'Py's initialization priority system.

**Acceptance Criteria**:
- Configuration (00a_) loads first with `init -10`
- Characters (00b_) load second with `init -5`
- Assets (00d*_) and variables (00c_) load at default priority (0)
- Logic (00e_), screens (00f_), and entry point (00g_) load last
- No `NameError` or `AttributeError` during game startup

**Rationale**: Ren'Py loads files alphabetically and by init priority. Incorrect ordering causes undefined reference errors.

---

### 1.3 Symbol Preservation

**Priority**: P0 (Critical)

The system shall preserve all symbol names, types, and values from the original `00_definiciones.rpy` file.

**Acceptance Criteria**:
- Every Character definition is preserved with identical properties
- Every variable has the same name, type, and default value
- Every asset (image, audio, transform) has the same identifier
- Every function has the same signature and behavior
- No symbols are duplicated across modules

**Rationale**: Changing symbol names or types would break all existing chapters and save files.

---

### 1.4 Backward Compatibility

**Priority**: P0 (Critical)

The system shall maintain full compatibility with existing game chapters and save files.

**Acceptance Criteria**:
- All chapters (prólogo, cap1) run without modification
- Save files created before modularization load successfully
- No regression in game behavior or visual appearance
- All narrative branches execute correctly

**Rationale**: The project has substantial existing content that cannot be rewritten.

---

### 1.5 Configuration Module

**Priority**: P0 (Critical)

The system shall provide a configuration module (`00a_configuracion.rpy`) containing all global constants and low-level initialization.

**Acceptance Criteria**:
- Defines color constants for all five characters (C_ICHIKA, C_NINO, C_MIKU, C_YOTSUBA, C_ITSUKI)
- Defines position constants for sprite formation (X_ICHIKA through X_ITSUKI)
- Registers the custom "ambiente" audio channel
- Initializes music volume to 1.0
- Loads with `init -10` priority

**Rationale**: Constants must be available before they are used in character definitions and assets.

---

### 1.6 Character Module

**Priority**: P0 (Critical)

The system shall provide a character module (`00b_personajes.rpy`) containing all Ren'Py Character definitions.

**Acceptance Criteria**:
- Defines main protagonist characters (mc, mc_pensamiento, narrador, narrator, profe)
- Defines all five quintuplet characters with proper styling
- Defines interior voice characters for Evento 6
- Defines secondary characters (isanari, raiha, maruo)
- Uses color constants from 00a_configuracion.rpy
- Uses helper functions from 07_ui.rpy (ui_personaje, ui_interior)
- Loads with `init -5` priority

**Rationale**: Character definitions depend on configuration constants and must load before they are used in narrative scripts.

---

### 1.7 Variable Module

**Priority**: P0 (Critical)

The system shall provide a variable module (`00c_variables.rpy`) containing all game state variables.

**Acceptance Criteria**:
- Defines player identity variables (nombre_jugador)
- Defines affinity points for all five characters (invisible to player)
- Defines tiebreaker variables (primera_conexion, primera_decision_hecha)
- Defines chapter 1 state variables (hub visits, chosen branches, flags)
- Defines Evento 6 state dictionaries
- Defines persistent variables for completed routes and unlocks
- All variables use `default` keyword for proper initialization
- Variables are organized by category with clear comments

**Rationale**: Centralizing variables makes state management clearer and reduces errors.

---

### 1.8 Asset Modules

**Priority**: P0 (Critical)

The system shall provide four specialized asset modules for multimedia content.

**Acceptance Criteria**:

**00d1_fondos.rpy**:
- Defines all background images (bg_*)
- Defines shared CG images used in multiple chapters
- Uses `Solid()` for simple backgrounds (bg_negro)

**00d2_sprites.rpy**:
- Defines all character sprite expressions
- Organizes by character with clear sections
- Documents pending assets with comments

**00d3_audio.rpy**:
- Defines background music tracks
- Defines character themes for each quintuplet
- Defines ambient audio loops
- Defines sound effects with proper categorization
- Defines UI interaction sounds

**00d4_transforms.rpy**:
- Defines sprite positioning transforms (pj, pj_habla, pj_calla)
- Defines scene transitions (mover, disolucion_lenta, fade_dia, corte_seco)
- Includes project rules in comments (always specify absolute position)
- All transforms explicitly declare xanchor, yanchor, xpos, ypos

**Rationale**: Separating assets by type makes them easier to find and update.

---

### 1.9 Logic Module

**Priority**: P0 (Critical)

The system shall provide a logic module (`00e_logica.rpy`) containing all Python helper functions.

**Acceptance Criteria**:
- Defines `sumar_punto(chica, cantidad)` for affinity management
- Defines `rutas_completadas()` to count finished routes
- Defines `rama_de(hermana)` to query chosen branch
- Defines `contar_ramas(tipo)` to count branches of a specific type
- Defines `duck(nivel, bajada, subida)` for audio ducking
- All functions have type hints
- All functions have docstrings documenting parameters, return values, and side effects
- Loads with `init python` block

**Rationale**: Centralizing game logic reduces code duplication and makes algorithms easier to test.

---

### 1.10 Screen Module

**Priority**: P0 (Critical)

The system shall provide a screen module (`00f_pantallas.rpy`) containing reusable UI screens.

**Acceptance Criteria**:
- Defines `screen pantalla_nombre()` for player name input
- Screen is modal with zorder 200
- Input field accepts only letters (Spanish), spaces, hyphens, apostrophes
- Maximum length is 16 characters
- Default value is "Futaro" if field is empty
- Enter key confirms input
- Screen updates both `nombre_jugador` and `persistent.nombre_jugador`

**Rationale**: Reusable screens reduce duplication and ensure consistent UI behavior.

---

### 1.11 Entry Point Module

**Priority**: P0 (Critical)

The system shall provide an entry point module (`00g_inicio.rpy`) containing `label start` and initialization logic.

**Acceptance Criteria**:
- Defines `label configurar_nombre` to handle name input
- Defines `label start` as the game entry point
- `label start` stops music with fadeout
- `label start` calls `configurar_nombre`
- `label start` jumps to `prologo`
- This is the ONLY `label start` in the entire project
- The label trims whitespace from player name
- Empty names default to "Futaro"

**Rationale**: A single, well-defined entry point prevents confusion and ensures consistent game startup.

---

### 1.12 Orchestrator File

**Priority**: P1 (High)

The system shall provide an orchestrator file (`00_definiciones.rpy`) that documents the new modular structure.

**Acceptance Criteria**:
- Contains header comment with project metadata
- Lists all module files with their responsibilities
- Explains the loading order and naming convention
- Warns against renaming files without verifying dependencies
- Contains NO executable code (only comments)
- Maintains the original filename for compatibility

**Rationale**: The orchestrator serves as a map for developers navigating the modular structure.

---

### 2. Non-Functional Requirements

### 2.1 Performance

**Priority**: P1 (High)

The system shall not significantly increase game compilation or startup time.

**Acceptance Criteria**:
- Compilation time increase is ≤ 50% (e.g., 100ms → 150ms)
- Startup time increase is imperceptible to users (< 200ms)
- Memory usage remains unchanged (Ren'Py loads everything at startup)
- No runtime performance degradation

**Rationale**: Modularization should improve developer experience without hurting player experience.

---

### 2.2 Maintainability

**Priority**: P0 (Critical)

The system shall significantly improve code maintainability and developer productivity.

**Acceptance Criteria**:
- Finding a specific definition takes < 30 seconds (vs. 2-3 minutes in monolithic file)
- Adding a new asset requires editing only one module (vs. searching through entire file)
- Merge conflicts are isolated to specific modules (80% reduction in conflict scope)
- New developers can understand the structure in < 15 minutes

**Rationale**: This is the primary goal of modularization.

---

### 2.3 Scalability

**Priority**: P1 (High)

The system shall support the addition of new chapters and content without requiring restructuring.

**Acceptance Criteria**:
- Adding new characters requires editing only 00b_personajes.rpy
- Adding new sprites requires editing only 00d2_sprites.rpy
- Adding new music requires editing only 00d3_audio.rpy
- Adding new game logic requires editing only 00e_logica.rpy
- The modular structure remains clear even with 5x more content

**Rationale**: The project will grow from ~1000 to ~5000 lines over its lifetime.

---

### 2.4 Testability

**Priority**: P1 (High)

The system shall enable comprehensive testing of individual modules and integration points.

**Acceptance Criteria**:
- Each module can be linted independently
- Symbol existence can be verified programmatically
- Dependencies can be validated through static analysis
- Integration tests can verify end-to-end functionality
- Test coverage reaches 100% of modules and 90% of symbols

**Rationale**: Testing prevents regressions and catches errors early.

---

### 2.5 Documentation

**Priority**: P1 (High)

The system shall be thoroughly documented at multiple levels.

**Acceptance Criteria**:
- Each module has a header comment explaining its purpose
- Each major section within a module has explanatory comments
- The orchestrator file documents the overall structure
- A separate ARCHITECTURE.md file provides a high-level overview
- Inline comments explain non-obvious design decisions
- Comments are in Spanish (project language)

**Rationale**: Good documentation reduces onboarding time and prevents misunderstandings.

---

### 2.6 Version Control Friendliness

**Priority**: P1 (High)

The system shall minimize merge conflicts and enable parallel development.

**Acceptance Criteria**:
- Two developers can work on different asset types without conflicts
- Changes to sprites don't conflict with changes to audio
- Git diffs are localized to relevant modules
- File rename history is preserved in version control

**Rationale**: Multiple developers will work on the project simultaneously.

---

### 3. Migration Requirements

### 3.1 Migration Process

**Priority**: P0 (Critical)

The system shall provide a clear, step-by-step migration process from the monolithic file to the modular structure.

**Acceptance Criteria**:
- Migration plan is documented with time estimates
- Each step has clear deliverables and success criteria
- Dependencies between steps are explicit
- The process can be executed in 4-6 hours by a single developer
- A rollback strategy is documented for each phase

**Rationale**: A clear process reduces risk and ensures consistent execution.

---

### 3.2 Data Preservation

**Priority**: P0 (Critical)

The system shall preserve all data during migration with zero loss.

**Acceptance Criteria**:
- All 600 lines of 00_definiciones.rpy are accounted for
- No definitions are accidentally deleted
- No definitions are accidentally modified
- A line-by-line mapping exists from source to destination
- Verification scripts confirm 100% coverage

**Rationale**: Losing definitions would break the game.

---

### 3.3 Backup and Recovery

**Priority**: P0 (Critical)

The system shall provide robust backup and recovery mechanisms.

**Acceptance Criteria**:
- A full backup of 00_definiciones.rpy is created before migration
- The backup is stored in a safe location (version control)
- Recovery instructions are documented and tested
- Recovery can be executed in < 5 minutes
- The game functions normally after recovery

**Rationale**: Migration might fail, and quick recovery prevents extended downtime.

---

### 3.4 Incremental Validation

**Priority**: P0 (Critical)

The system shall validate each module immediately after creation.

**Acceptance Criteria**:
- `renpy.lint()` is executed after each module is created
- Compilation errors are fixed before proceeding to the next module
- Symbol existence is verified programmatically
- Type checking is performed on all definitions
- No module is considered "done" until validation passes

**Rationale**: Early validation catches errors before they compound.

---

### 4. Quality Requirements

### 4.1 Code Quality

**Priority**: P1 (High)

The system shall maintain high code quality standards.

**Acceptance Criteria**:
- All Python code follows PEP 8 style guidelines (where applicable to Ren'Py)
- All functions have docstrings
- All magic numbers are replaced with named constants
- No commented-out code (except documented pending features)
- Consistent indentation (4 spaces)
- Consistent naming conventions (snake_case for variables, PascalCase for constants)

**Rationale**: High-quality code is easier to maintain and less error-prone.

---

### 4.2 Consistency

**Priority**: P1 (High)

The system shall maintain consistency across all modules.

**Acceptance Criteria**:
- All modules use the same header comment format
- All modules use consistent indentation and spacing
- All modules follow the same naming conventions
- All modules document their dependencies in comments
- All modules include rationale for non-obvious decisions

**Rationale**: Consistency reduces cognitive load when switching between modules.

---

### 4.3 Error Handling

**Priority**: P1 (High)

The system shall handle common error scenarios gracefully.

**Acceptance Criteria**:
- Undefined references are caught at compile time
- Missing assets generate clear warnings
- Duplicate definitions are detected and reported
- Load order errors provide diagnostic information
- Recovery instructions are included in error messages

**Rationale**: Clear error messages speed up debugging.

---

### 5. Constraints

### 5.1 Technical Constraints

**Priority**: P0 (Critical)

The system must operate within Ren'Py's technical constraints.

**Acceptance Criteria**:
- Compatible with Ren'Py 8.5.3 or later
- Uses only Ren'Py-supported Python features (Python 3.9)
- Respects Ren'Py's file loading order (alphabetical + init priority)
- Uses only Ren'Py-supported file extensions (.rpy, .rpyc)
- Does not exceed Ren'Py's practical limits (file count, symbol count)

**Rationale**: The system must work within the Ren'Py engine.

---

### 5.2 Project Constraints

**Priority**: P0 (Critical)

The system must respect existing project conventions and structure.

**Acceptance Criteria**:
- Modules are placed in the `game/` directory
- Naming follows the existing `00_`, `01_`, `02_` prefix pattern
- Spanish is used for all comments and documentation
- The project's visual style and UX remain unchanged
- No breaking changes to the public API (labels, variables visible to chapters)

**Rationale**: The modularization must fit seamlessly into the existing project.

---

### 5.3 Timeline Constraints

**Priority**: P1 (High)

The migration must be completed within a single work session.

**Acceptance Criteria**:
- Total migration time is 4-6 hours
- No phase takes longer than 3 hours
- Testing is completed within the timeline
- Documentation is updated before the session ends

**Rationale**: A long-running migration increases risk of conflicts and incomplete work.

---

### 6. Success Metrics

### 6.1 Developer Productivity

**Priority**: P1 (High)

The system shall measurably improve developer productivity.

**Success Criteria**:
- Time to find a definition: 30s (vs. 2-3 min baseline)
- Time to add a new asset: 1 min (vs. 5 min baseline)
- Merge conflict rate: 20% (vs. 100% baseline)
- Onboarding time for new developer: 15 min (vs. 60 min baseline)

**Measurement**: Time trials before and after modularization.

---

### 6.2 Code Quality Metrics

**Priority**: P1 (High)

The system shall maintain or improve code quality metrics.

**Success Criteria**:
- `renpy.lint()` warnings: 0 critical warnings
- Code duplication: 0% (no duplicate definitions)
- Average module size: < 100 lines (vs. 600-line monolith)
- Comment density: > 20% of lines

**Measurement**: Static analysis tools and manual review.

---

### 6.3 Stability Metrics

**Priority**: P0 (Critical)

The system shall maintain or improve game stability.

**Success Criteria**:
- Crash rate: 0 (no new crashes introduced)
- Regression count: 0 (no existing features broken)
- Save compatibility: 100% (all old saves load)
- Compilation success rate: 100%

**Measurement**: Integration testing and user testing.

---

### 7. Open Questions

### 7.1 Asset Organization

**Question**: Should assets be further subdivided by character (e.g., 00d2a_sprites_ichika.rpy)?

**Options**:
1. Keep current four-file structure (00d1-00d4)
2. Subdivide sprites by character (5 additional files)

**Decision Criteria**: Current sprite count (25) doesn't justify additional files. Revisit if count exceeds 50.

**Status**: Deferred to future iteration.

---

### 7.2 Future Chapter Integration

**Question**: Should future chapters follow a similar modular pattern (e.g., 02_cap1 split into 02a, 02b, 02c)?

**Options**:
1. Apply modularization only to shared definitions (00_*)
2. Apply modularization to all chapters (01_*, 02_*, etc.)

**Decision Criteria**: Evaluate after completing 00_ modularization and observing impact.

**Status**: Deferred pending user feedback.

---

### 7.3 Automated Testing

**Question**: Should automated tests be added for symbol existence and type checking?

**Options**:
1. Manual testing only (current approach)
2. Add pytest-based test suite for validation

**Decision Criteria**: Project complexity and team size. Small team may not justify automation.

**Status**: Recommended but not required for initial migration.

---

### 8. Dependencies on External Requirements

This feature has no dependencies on external requirements from other features. It is a self-contained refactoring project.

---

### 9. Approval and Sign-off

**Requirements Author**: AI Assistant (Kiro)  
**Date**: 2026-05-11  
**Status**: Draft - Awaiting User Review

**Review Checklist**:
- [ ] All functional requirements are clear and testable
- [ ] Non-functional requirements have measurable criteria
- [ ] Migration process is detailed and realistic
- [ ] Success metrics are defined
- [ ] Open questions are documented
- [ ] User approves and signs off

---

## Glossary

**Ren'Py**: Visual novel game engine used by the project  
**ATL**: Animation and Transformation Language (Ren'Py's animation system)  
**Character**: Ren'Py object representing a speaking character  
**Transform**: Ren'Py object defining sprite positioning and animation  
**Init Priority**: Number determining load order (-10 = earliest, 0 = default)  
**Store**: Ren'Py's global variable namespace  
**Persistent**: Variables that survive between game sessions  
**Label**: Ren'Py's equivalent of a function or scene  
**CG**: Computer Graphics (full-screen illustrations)  
**Sprite**: Character images with transparent backgrounds  
**Hub**: Branching point where player chooses which character to interact with  
**Evento 6**: Special event at the end of Chapter 1 with minigames
