class Colors:
    INFO = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    ERROR = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

    reference = "https://www.delftstack.com/ko/howto/python/python-print-colored-text/"

    before_weight = 0


def info(key, weight):
    if weight == Colors.before_weight:
        print(f"{Colors.INFO}[INFO] key: {key} weight: {weight}{Colors.RESET}")
    else:
        print(f"\n{Colors.INFO}[INFO] key: {key} weight: {weight} (diff: {weight - Colors.before_weight}){Colors.RESET}")
        Colors.before_weight = weight


def when_none_element_found(weight):
    print(f"{Colors.WARNING}[WARN] none element detected {weight}{Colors.RESET}")


def when_key_is_not_in_comparison_target(key, weight):
    print(f"{Colors.WARNING}[WARN] {key} is not in comparison target with weight: {weight}{Colors.RESET}")


def when_key_is_not_equal_to_comparison_target(key, weight, target_key, comp_target_key):
    print(f"{Colors.WARNING}[WARN] key: {key} value: \"{target_key}\" is not equal to \"{comp_target_key}\" with weight: {weight}")


def when_dict_is_not_in_comparison_target(dict_, weight):
    print(f"{Colors.WARNING}[WARN] {dict_} is not in comparison target with weight: {weight}{Colors.RESET}")


def final_score(num):
    print(f"\n{Colors.INFO}[INFO] final score: {1 - num}{Colors.RESET}")


def error(error_massage):
    print(f"{Colors.ERROR}[ERROR] {error_massage}{Colors.RESET}")
