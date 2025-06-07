# tests/test_batches.py

from datetime import date
from src.model import Batch, OrderLine

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

def test_allocating_to_a_batch_reduces_available_quantity():
    batch = Batch("batch-001", "CHAIR", 20, eta=date.today())
    line = OrderLine("order-001", "CHAIR", 2)
    batch.allocate(line)
    assert batch.available_quantity == 18

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "CHAIR", 10, eta=None)
    line = OrderLine("order-002", "TABLE", 1)
    assert batch.can_allocate(line) is False

def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("LAMP", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18

def test_can_deallocate_allocated_lines():
    batch, line = make_batch_and_line("DESK", 20, 2)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 20

def test_cannot_deallocate_unallocated_lines():
    batch, unallocated_line = make_batch_and_line("SHELF", 20, 2)
    batch.deallocate(unallocated_line)  # nothing should happen
    assert batch.available_quantity == 20
