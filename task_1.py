from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    constraints = PrinterConstraints(**constraints)
    
    sorted_jobs = sorted(jobs, key=lambda x: x.priority)
    
    batches = []
    current_batch = []
    current_volume = 0.0
    current_count = 0
    
    for job in sorted_jobs:
        if (current_volume + job.volume <= constraints.max_volume and 
            current_count + 1 <= constraints.max_items):
            current_batch.append(job)
            current_volume += job.volume
            current_count += 1
        else:
            if current_batch:
                batches.append(current_batch)
            current_batch = [job]
            current_volume = job.volume
            current_count = 1
    
    if current_batch:
        batches.append(current_batch)
    
    print_order = []
    total_time = 0
    for batch in batches:
        total_time += max(job.print_time for job in batch)
        for job in batch:
            print_order.append(job.id)
    
    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Testing
def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} minutes")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} minutes")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()