"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2010-2024 Google LLC
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BopOptimizerMethod(google.protobuf.message.Message):
    """Method used to optimize a solution in Bop.

    NEXT TAG: 16
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _OptimizerType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OptimizerTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[BopOptimizerMethod._OptimizerType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SAT_CORE_BASED: BopOptimizerMethod._OptimizerType.ValueType  # 0
        SAT_LINEAR_SEARCH: BopOptimizerMethod._OptimizerType.ValueType  # 15
        LINEAR_RELAXATION: BopOptimizerMethod._OptimizerType.ValueType  # 1
        LOCAL_SEARCH: BopOptimizerMethod._OptimizerType.ValueType  # 2
        RANDOM_FIRST_SOLUTION: BopOptimizerMethod._OptimizerType.ValueType  # 3
        RANDOM_CONSTRAINT_LNS: BopOptimizerMethod._OptimizerType.ValueType  # 4
        RANDOM_VARIABLE_LNS: BopOptimizerMethod._OptimizerType.ValueType  # 5
        COMPLETE_LNS: BopOptimizerMethod._OptimizerType.ValueType  # 7
        LP_FIRST_SOLUTION: BopOptimizerMethod._OptimizerType.ValueType  # 8
        OBJECTIVE_FIRST_SOLUTION: BopOptimizerMethod._OptimizerType.ValueType  # 9
        USER_GUIDED_FIRST_SOLUTION: BopOptimizerMethod._OptimizerType.ValueType  # 14
        RANDOM_CONSTRAINT_LNS_GUIDED_BY_LP: BopOptimizerMethod._OptimizerType.ValueType  # 11
        RANDOM_VARIABLE_LNS_GUIDED_BY_LP: BopOptimizerMethod._OptimizerType.ValueType  # 12
        RELATION_GRAPH_LNS: BopOptimizerMethod._OptimizerType.ValueType  # 16
        RELATION_GRAPH_LNS_GUIDED_BY_LP: BopOptimizerMethod._OptimizerType.ValueType  # 17

    class OptimizerType(_OptimizerType, metaclass=_OptimizerTypeEnumTypeWrapper): ...
    SAT_CORE_BASED: BopOptimizerMethod.OptimizerType.ValueType  # 0
    SAT_LINEAR_SEARCH: BopOptimizerMethod.OptimizerType.ValueType  # 15
    LINEAR_RELAXATION: BopOptimizerMethod.OptimizerType.ValueType  # 1
    LOCAL_SEARCH: BopOptimizerMethod.OptimizerType.ValueType  # 2
    RANDOM_FIRST_SOLUTION: BopOptimizerMethod.OptimizerType.ValueType  # 3
    RANDOM_CONSTRAINT_LNS: BopOptimizerMethod.OptimizerType.ValueType  # 4
    RANDOM_VARIABLE_LNS: BopOptimizerMethod.OptimizerType.ValueType  # 5
    COMPLETE_LNS: BopOptimizerMethod.OptimizerType.ValueType  # 7
    LP_FIRST_SOLUTION: BopOptimizerMethod.OptimizerType.ValueType  # 8
    OBJECTIVE_FIRST_SOLUTION: BopOptimizerMethod.OptimizerType.ValueType  # 9
    USER_GUIDED_FIRST_SOLUTION: BopOptimizerMethod.OptimizerType.ValueType  # 14
    RANDOM_CONSTRAINT_LNS_GUIDED_BY_LP: BopOptimizerMethod.OptimizerType.ValueType  # 11
    RANDOM_VARIABLE_LNS_GUIDED_BY_LP: BopOptimizerMethod.OptimizerType.ValueType  # 12
    RELATION_GRAPH_LNS: BopOptimizerMethod.OptimizerType.ValueType  # 16
    RELATION_GRAPH_LNS_GUIDED_BY_LP: BopOptimizerMethod.OptimizerType.ValueType  # 17

    TYPE_FIELD_NUMBER: builtins.int
    type: global___BopOptimizerMethod.OptimizerType.ValueType
    def __init__(
        self,
        *,
        type: global___BopOptimizerMethod.OptimizerType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["type", b"type"]) -> None: ...

global___BopOptimizerMethod = BopOptimizerMethod

@typing.final
class BopSolverOptimizerSet(google.protobuf.message.Message):
    """Set of optimizer methods to be run by an instance of the portfolio optimizer.
    Note that in the current implementation, all the methods specified in the
    repeated field methods will run on the same solver / thread.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METHODS_FIELD_NUMBER: builtins.int
    @property
    def methods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BopOptimizerMethod]: ...
    def __init__(
        self,
        *,
        methods: collections.abc.Iterable[global___BopOptimizerMethod] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["methods", b"methods"]) -> None: ...

global___BopSolverOptimizerSet = BopSolverOptimizerSet

@typing.final
class BopParameters(google.protobuf.message.Message):
    """Contains the definitions for all the bop algorithm parameters and their
    default values.

    NEXT TAG: 42
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ThreadSynchronizationType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ThreadSynchronizationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[BopParameters._ThreadSynchronizationType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NO_SYNCHRONIZATION: BopParameters._ThreadSynchronizationType.ValueType  # 0
        """No synchronization. The solvers run independently until the time limit
        is reached; Then learned information from each solver are aggregated.
        The final solution is the best of all found solutions.
        Pros: - No need to wait for another solver to complete its task,
              - Adding a new solver always improves the final solution (In the
                current implementation it still depends on the machine load and
                the time limit).
        Cons: - No learning between solvers.
        """
        SYNCHRONIZE_ALL: BopParameters._ThreadSynchronizationType.ValueType  # 1
        """Synchronize all solvers. Each solver waits for all other solvers to
        complete the previous optimizer run, before running again.
        The final solution is the best of all found solutions.
        Pros: - Full learning between solvers.
        Cons: - A lot of waiting time when solvers don't run at the exact same
                speed,
              - The quality of the final solution depends on the number of
                solvers, adding one more solver might lead to poorer results
                because the search goes on a different path.
        """
        SYNCHRONIZE_ON_RIGHT: BopParameters._ThreadSynchronizationType.ValueType  # 2
        """Solver i synchronizes with solvers 0..i-1.
        This is a good tradeoff between NO_SYNCHRONIZATION and SYNCHRONIZE_ALL:
        communication while keeping a relative determinism on the result even
        when the number of solvers increases.
        The final solution is the best of all found solutions.
        Pros: - Solver i learns from i different solvers,
              - Adding a new solver always improves the final solution (In the
                current implementation it still depends on the machine load and
                the time limit).
        Cons: - No full learning,
              - Some solvers need to wait for synchronization.
        """

    class ThreadSynchronizationType(_ThreadSynchronizationType, metaclass=_ThreadSynchronizationTypeEnumTypeWrapper):
        """Defines how the different solvers are synchronized during the search.
        Note that the synchronization (if any) occurs before each call to an
        optimizer (the smallest granularity of the solver in a parallel context).
        """

    NO_SYNCHRONIZATION: BopParameters.ThreadSynchronizationType.ValueType  # 0
    """No synchronization. The solvers run independently until the time limit
    is reached; Then learned information from each solver are aggregated.
    The final solution is the best of all found solutions.
    Pros: - No need to wait for another solver to complete its task,
          - Adding a new solver always improves the final solution (In the
            current implementation it still depends on the machine load and
            the time limit).
    Cons: - No learning between solvers.
    """
    SYNCHRONIZE_ALL: BopParameters.ThreadSynchronizationType.ValueType  # 1
    """Synchronize all solvers. Each solver waits for all other solvers to
    complete the previous optimizer run, before running again.
    The final solution is the best of all found solutions.
    Pros: - Full learning between solvers.
    Cons: - A lot of waiting time when solvers don't run at the exact same
            speed,
          - The quality of the final solution depends on the number of
            solvers, adding one more solver might lead to poorer results
            because the search goes on a different path.
    """
    SYNCHRONIZE_ON_RIGHT: BopParameters.ThreadSynchronizationType.ValueType  # 2
    """Solver i synchronizes with solvers 0..i-1.
    This is a good tradeoff between NO_SYNCHRONIZATION and SYNCHRONIZE_ALL:
    communication while keeping a relative determinism on the result even
    when the number of solvers increases.
    The final solution is the best of all found solutions.
    Pros: - Solver i learns from i different solvers,
          - Adding a new solver always improves the final solution (In the
            current implementation it still depends on the machine load and
            the time limit).
    Cons: - No full learning,
          - Some solvers need to wait for synchronization.
    """

    MAX_TIME_IN_SECONDS_FIELD_NUMBER: builtins.int
    MAX_DETERMINISTIC_TIME_FIELD_NUMBER: builtins.int
    LP_MAX_DETERMINISTIC_TIME_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_CONSECUTIVE_FAILING_OPTIMIZER_CALLS_FIELD_NUMBER: builtins.int
    RELATIVE_GAP_LIMIT_FIELD_NUMBER: builtins.int
    MAX_NUM_DECISIONS_IN_LS_FIELD_NUMBER: builtins.int
    MAX_NUM_BROKEN_CONSTRAINTS_IN_LS_FIELD_NUMBER: builtins.int
    LOG_SEARCH_PROGRESS_FIELD_NUMBER: builtins.int
    COMPUTE_ESTIMATED_IMPACT_FIELD_NUMBER: builtins.int
    PRUNE_SEARCH_TREE_FIELD_NUMBER: builtins.int
    SORT_CONSTRAINTS_BY_NUM_TERMS_FIELD_NUMBER: builtins.int
    USE_RANDOM_LNS_FIELD_NUMBER: builtins.int
    RANDOM_SEED_FIELD_NUMBER: builtins.int
    NUM_RELAXED_VARS_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_CONFLICTS_IN_RANDOM_LNS_FIELD_NUMBER: builtins.int
    NUM_RANDOM_LNS_TRIES_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_BACKTRACKS_IN_LS_FIELD_NUMBER: builtins.int
    USE_LP_LNS_FIELD_NUMBER: builtins.int
    USE_SAT_TO_CHOOSE_LNS_NEIGHBOURHOOD_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_CONFLICTS_FOR_QUICK_CHECK_FIELD_NUMBER: builtins.int
    USE_SYMMETRY_FIELD_NUMBER: builtins.int
    EXPLOIT_SYMMETRY_IN_SAT_FIRST_SOLUTION_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_CONFLICTS_IN_RANDOM_SOLUTION_GENERATION_FIELD_NUMBER: builtins.int
    MAX_NUMBER_OF_EXPLORED_ASSIGNMENTS_PER_TRY_IN_LS_FIELD_NUMBER: builtins.int
    USE_TRANSPOSITION_TABLE_IN_LS_FIELD_NUMBER: builtins.int
    USE_POTENTIAL_ONE_FLIP_REPAIRS_IN_LS_FIELD_NUMBER: builtins.int
    USE_LEARNED_BINARY_CLAUSES_IN_LP_FIELD_NUMBER: builtins.int
    NUMBER_OF_SOLVERS_FIELD_NUMBER: builtins.int
    SYNCHRONIZATION_TYPE_FIELD_NUMBER: builtins.int
    SOLVER_OPTIMIZER_SETS_FIELD_NUMBER: builtins.int
    DEFAULT_SOLVER_OPTIMIZER_SETS_FIELD_NUMBER: builtins.int
    USE_LP_STRONG_BRANCHING_FIELD_NUMBER: builtins.int
    DECOMPOSER_NUM_VARIABLES_THRESHOLD_FIELD_NUMBER: builtins.int
    NUM_BOP_SOLVERS_USED_BY_DECOMPOSITION_FIELD_NUMBER: builtins.int
    DECOMPOSED_PROBLEM_MIN_TIME_IN_SECONDS_FIELD_NUMBER: builtins.int
    GUIDED_SAT_CONFLICTS_CHUNK_FIELD_NUMBER: builtins.int
    MAX_LP_SOLVE_FOR_FEASIBILITY_PROBLEMS_FIELD_NUMBER: builtins.int
    max_time_in_seconds: builtins.float
    """Maximum time allowed in seconds to solve a problem.
    The counter will starts as soon as Solve() is called.
    """
    max_deterministic_time: builtins.float
    """Maximum time allowed in deterministic time to solve a problem.
    The deterministic time should be correlated with the real time used by the
    solver, the time unit being roughly the order of magnitude of a second.
    The counter will starts as soon as SetParameters() or SolveWithTimeLimit()
    is called.
    """
    lp_max_deterministic_time: builtins.float
    """The max deterministic time given to the LP solver each time it is called.
    If this is not enough to solve the LP at hand, it will simply be called
    again later (and the solve will resume from where it stopped).
    """
    max_number_of_consecutive_failing_optimizer_calls: builtins.int
    """Maximum number of consecutive optimizer calls without improving the
    current solution. If this number is reached, the search will be aborted.
    Note that this parameter only applies when an initial solution has been
    found or is provided. Also note that there is no limit to the number of
    calls, when the parameter is not set.
    """
    relative_gap_limit: builtins.float
    """Limit used to stop the optimization as soon as the relative gap is smaller
    than the given value.
    The relative gap is defined as:
      abs(solution_cost - best_bound)
           / max(abs(solution_cost), abs(best_bound)).
    """
    max_num_decisions_in_ls: builtins.int
    """Maximum number of cascading decisions the solver might use to repair the
    current solution in the LS.
    """
    max_num_broken_constraints_in_ls: builtins.int
    """Abort the LS search tree as soon as strictly more than this number of
    constraints are broken. The default is a large value which basically
    disable this heuristic.
    """
    log_search_progress: builtins.bool
    """Whether the solver should log the search progress to LOG(INFO)."""
    compute_estimated_impact: builtins.bool
    """Compute estimated impact at each iteration when true; only once when false."""
    prune_search_tree: builtins.bool
    """Avoid exploring both branches (b, a, ...) and (a, b, ...)."""
    sort_constraints_by_num_terms: builtins.bool
    """Sort constraints by increasing total number of terms instead of number of
    contributing terms.
    """
    use_random_lns: builtins.bool
    """Use the random Large Neighborhood Search instead of the exhaustive one."""
    random_seed: builtins.int
    """The seed used to initialize the random generator.

    TODO(user): Some of our client test fail depending on this value! we need
    to fix them and ideally randomize our behavior from on test to the next so
    that this doesn't happen in the future.
    """
    num_relaxed_vars: builtins.int
    """Number of variables to relax in the exhaustive Large Neighborhood Search."""
    max_number_of_conflicts_in_random_lns: builtins.int
    """The number of conflicts the SAT solver has to solve a random LNS
    subproblem.
    """
    num_random_lns_tries: builtins.int
    """Number of tries in the random lns."""
    max_number_of_backtracks_in_ls: builtins.int
    """Maximum number of backtracks times the number of variables in Local Search,
    ie. max num backtracks == max_number_of_backtracks_in_ls / num variables.
    """
    use_lp_lns: builtins.bool
    """Use Large Neighborhood Search based on the LP relaxation."""
    use_sat_to_choose_lns_neighbourhood: builtins.bool
    """Whether we use sat propagation to choose the lns neighbourhood."""
    max_number_of_conflicts_for_quick_check: builtins.int
    """The number of conflicts the SAT solver has to solve a random LNS
    subproblem for the quick check of infeasibility.
    """
    use_symmetry: builtins.bool
    """If true, find and exploit the eventual symmetries of the problem.

    TODO(user): turn this on by default once the symmetry finder becomes fast
    enough to be negligeable for most problem. Or at least support a time
    limit.
    """
    exploit_symmetry_in_sat_first_solution: builtins.bool
    """If true, find and exploit symmetries in proving satisfiability in the first
    problem.
    This feature is experimental. On some problems, computing symmetries may
    run forever. You may also run into unforseen problems as this feature was
    not extensively tested.
    """
    max_number_of_conflicts_in_random_solution_generation: builtins.int
    """The number of conflicts the SAT solver has to generate a random solution."""
    max_number_of_explored_assignments_per_try_in_ls: builtins.int
    """The maximum number of assignments the Local Search iterates on during one
    try. Note that if the Local Search is called again on the same solution
    it will not restart from scratch but will iterate on the next
    max_number_of_explored_assignments_per_try_in_ls assignments.
    """
    use_transposition_table_in_ls: builtins.bool
    """Whether we use an hash set during the LS to avoid exploring more than once
    the "same" state. Note that because the underlying SAT solver may learn
    information in the middle of the LS, this may make the LS slightly less
    "complete", but it should be faster.
    """
    use_potential_one_flip_repairs_in_ls: builtins.bool
    """Whether we keep a list of variable that can potentially repair in one flip
    all the current infeasible constraints (such variable must at least appear
    in all the infeasible constraints for this to happen).
    """
    use_learned_binary_clauses_in_lp: builtins.bool
    """Whether we use the learned binary clauses in the Linear Relaxation."""
    number_of_solvers: builtins.int
    """The number of solvers used to run Bop. Note that one thread will be created
    per solver. The type of communication between solvers is specified by the
    synchronization_type parameter.
    """
    synchronization_type: global___BopParameters.ThreadSynchronizationType.ValueType
    default_solver_optimizer_sets: builtins.str
    use_lp_strong_branching: builtins.bool
    """Use strong branching in the linear relaxation optimizer.
    The strong branching is a what-if analysis on each variable v, i.e.
    compute the best bound when v is assigned to true, compute the best bound
    when v is assigned to false, and then use those best bounds to improve the
    overall best bound.
    This is useful to improve the best_bound, but also to fix some variables
    during search.
    Note that using probing might be time consuming as it runs the LP solver
    2 * num_variables times.
    """
    decomposer_num_variables_threshold: builtins.int
    """Only try to decompose the problem when the number of variables is greater
    than the threshold.
    """
    num_bop_solvers_used_by_decomposition: builtins.int
    """The number of BopSolver created (thread pool workers) used by the integral
    solver to solve a decomposed problem.
    TODO(user): Merge this with the number_of_solvers parameter.
    """
    decomposed_problem_min_time_in_seconds: builtins.float
    """HACK. To avoid spending too little time on small problems, spend at least
    this time solving each of the decomposed sub-problem. This only make sense
    if num_bop_solvers_used_by_decomposition is greater than 1 so that the
    overhead can be "absorbed" by the other threads.
    """
    guided_sat_conflicts_chunk: builtins.int
    """The first solutions based on guided SAT will work in chunk of that many
    conflicts at the time. This allows to simulate parallelism between the
    different guiding strategy on a single core.
    """
    max_lp_solve_for_feasibility_problems: builtins.int
    """The maximum number of time the LP solver will run to feasibility for pure
    feasibility problems (with a constant-valued objective function). Set this
    to a small value, e.g., 1, if fractional solutions offer useful guidance to
    other solvers in the portfolio. A negative value means no limit.
    """
    @property
    def solver_optimizer_sets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BopSolverOptimizerSet]:
        """List of set of optimizers to be run by the solvers.
        Note that the i_th solver will run the
        min(i, solver_optimizer_sets_size())_th optimizer set.
        The default is defined by default_solver_optimizer_sets (only one set).
        """

    def __init__(
        self,
        *,
        max_time_in_seconds: builtins.float | None = ...,
        max_deterministic_time: builtins.float | None = ...,
        lp_max_deterministic_time: builtins.float | None = ...,
        max_number_of_consecutive_failing_optimizer_calls: builtins.int | None = ...,
        relative_gap_limit: builtins.float | None = ...,
        max_num_decisions_in_ls: builtins.int | None = ...,
        max_num_broken_constraints_in_ls: builtins.int | None = ...,
        log_search_progress: builtins.bool | None = ...,
        compute_estimated_impact: builtins.bool | None = ...,
        prune_search_tree: builtins.bool | None = ...,
        sort_constraints_by_num_terms: builtins.bool | None = ...,
        use_random_lns: builtins.bool | None = ...,
        random_seed: builtins.int | None = ...,
        num_relaxed_vars: builtins.int | None = ...,
        max_number_of_conflicts_in_random_lns: builtins.int | None = ...,
        num_random_lns_tries: builtins.int | None = ...,
        max_number_of_backtracks_in_ls: builtins.int | None = ...,
        use_lp_lns: builtins.bool | None = ...,
        use_sat_to_choose_lns_neighbourhood: builtins.bool | None = ...,
        max_number_of_conflicts_for_quick_check: builtins.int | None = ...,
        use_symmetry: builtins.bool | None = ...,
        exploit_symmetry_in_sat_first_solution: builtins.bool | None = ...,
        max_number_of_conflicts_in_random_solution_generation: builtins.int | None = ...,
        max_number_of_explored_assignments_per_try_in_ls: builtins.int | None = ...,
        use_transposition_table_in_ls: builtins.bool | None = ...,
        use_potential_one_flip_repairs_in_ls: builtins.bool | None = ...,
        use_learned_binary_clauses_in_lp: builtins.bool | None = ...,
        number_of_solvers: builtins.int | None = ...,
        synchronization_type: global___BopParameters.ThreadSynchronizationType.ValueType | None = ...,
        solver_optimizer_sets: collections.abc.Iterable[global___BopSolverOptimizerSet] | None = ...,
        default_solver_optimizer_sets: builtins.str | None = ...,
        use_lp_strong_branching: builtins.bool | None = ...,
        decomposer_num_variables_threshold: builtins.int | None = ...,
        num_bop_solvers_used_by_decomposition: builtins.int | None = ...,
        decomposed_problem_min_time_in_seconds: builtins.float | None = ...,
        guided_sat_conflicts_chunk: builtins.int | None = ...,
        max_lp_solve_for_feasibility_problems: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["compute_estimated_impact", b"compute_estimated_impact", "decomposed_problem_min_time_in_seconds", b"decomposed_problem_min_time_in_seconds", "decomposer_num_variables_threshold", b"decomposer_num_variables_threshold", "default_solver_optimizer_sets", b"default_solver_optimizer_sets", "exploit_symmetry_in_sat_first_solution", b"exploit_symmetry_in_sat_first_solution", "guided_sat_conflicts_chunk", b"guided_sat_conflicts_chunk", "log_search_progress", b"log_search_progress", "lp_max_deterministic_time", b"lp_max_deterministic_time", "max_deterministic_time", b"max_deterministic_time", "max_lp_solve_for_feasibility_problems", b"max_lp_solve_for_feasibility_problems", "max_num_broken_constraints_in_ls", b"max_num_broken_constraints_in_ls", "max_num_decisions_in_ls", b"max_num_decisions_in_ls", "max_number_of_backtracks_in_ls", b"max_number_of_backtracks_in_ls", "max_number_of_conflicts_for_quick_check", b"max_number_of_conflicts_for_quick_check", "max_number_of_conflicts_in_random_lns", b"max_number_of_conflicts_in_random_lns", "max_number_of_conflicts_in_random_solution_generation", b"max_number_of_conflicts_in_random_solution_generation", "max_number_of_consecutive_failing_optimizer_calls", b"max_number_of_consecutive_failing_optimizer_calls", "max_number_of_explored_assignments_per_try_in_ls", b"max_number_of_explored_assignments_per_try_in_ls", "max_time_in_seconds", b"max_time_in_seconds", "num_bop_solvers_used_by_decomposition", b"num_bop_solvers_used_by_decomposition", "num_random_lns_tries", b"num_random_lns_tries", "num_relaxed_vars", b"num_relaxed_vars", "number_of_solvers", b"number_of_solvers", "prune_search_tree", b"prune_search_tree", "random_seed", b"random_seed", "relative_gap_limit", b"relative_gap_limit", "sort_constraints_by_num_terms", b"sort_constraints_by_num_terms", "synchronization_type", b"synchronization_type", "use_learned_binary_clauses_in_lp", b"use_learned_binary_clauses_in_lp", "use_lp_lns", b"use_lp_lns", "use_lp_strong_branching", b"use_lp_strong_branching", "use_potential_one_flip_repairs_in_ls", b"use_potential_one_flip_repairs_in_ls", "use_random_lns", b"use_random_lns", "use_sat_to_choose_lns_neighbourhood", b"use_sat_to_choose_lns_neighbourhood", "use_symmetry", b"use_symmetry", "use_transposition_table_in_ls", b"use_transposition_table_in_ls"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["compute_estimated_impact", b"compute_estimated_impact", "decomposed_problem_min_time_in_seconds", b"decomposed_problem_min_time_in_seconds", "decomposer_num_variables_threshold", b"decomposer_num_variables_threshold", "default_solver_optimizer_sets", b"default_solver_optimizer_sets", "exploit_symmetry_in_sat_first_solution", b"exploit_symmetry_in_sat_first_solution", "guided_sat_conflicts_chunk", b"guided_sat_conflicts_chunk", "log_search_progress", b"log_search_progress", "lp_max_deterministic_time", b"lp_max_deterministic_time", "max_deterministic_time", b"max_deterministic_time", "max_lp_solve_for_feasibility_problems", b"max_lp_solve_for_feasibility_problems", "max_num_broken_constraints_in_ls", b"max_num_broken_constraints_in_ls", "max_num_decisions_in_ls", b"max_num_decisions_in_ls", "max_number_of_backtracks_in_ls", b"max_number_of_backtracks_in_ls", "max_number_of_conflicts_for_quick_check", b"max_number_of_conflicts_for_quick_check", "max_number_of_conflicts_in_random_lns", b"max_number_of_conflicts_in_random_lns", "max_number_of_conflicts_in_random_solution_generation", b"max_number_of_conflicts_in_random_solution_generation", "max_number_of_consecutive_failing_optimizer_calls", b"max_number_of_consecutive_failing_optimizer_calls", "max_number_of_explored_assignments_per_try_in_ls", b"max_number_of_explored_assignments_per_try_in_ls", "max_time_in_seconds", b"max_time_in_seconds", "num_bop_solvers_used_by_decomposition", b"num_bop_solvers_used_by_decomposition", "num_random_lns_tries", b"num_random_lns_tries", "num_relaxed_vars", b"num_relaxed_vars", "number_of_solvers", b"number_of_solvers", "prune_search_tree", b"prune_search_tree", "random_seed", b"random_seed", "relative_gap_limit", b"relative_gap_limit", "solver_optimizer_sets", b"solver_optimizer_sets", "sort_constraints_by_num_terms", b"sort_constraints_by_num_terms", "synchronization_type", b"synchronization_type", "use_learned_binary_clauses_in_lp", b"use_learned_binary_clauses_in_lp", "use_lp_lns", b"use_lp_lns", "use_lp_strong_branching", b"use_lp_strong_branching", "use_potential_one_flip_repairs_in_ls", b"use_potential_one_flip_repairs_in_ls", "use_random_lns", b"use_random_lns", "use_sat_to_choose_lns_neighbourhood", b"use_sat_to_choose_lns_neighbourhood", "use_symmetry", b"use_symmetry", "use_transposition_table_in_ls", b"use_transposition_table_in_ls"]) -> None: ...

global___BopParameters = BopParameters
