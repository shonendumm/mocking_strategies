import pytest

# Instead of returning data directly, the fixture instead returns a function which generates the data. This function can then be called multiple times in the test.

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")

# destroy the data after use
@pytest.fixture
def make_customer_record_two():
    created_records = []

    def _make_customer_record_two(name):
        record = {"name": name, "orders": []}
        created_records.append(record)
        return record

    # just to encure destroying the data after creation, use yield
    yield _make_customer_record_two

    for record in created_records:
        del record # delete the record


def test_customer_records_two(make_customer_record_two):
    customer_1 = make_customer_record_two("Lisa")
    customer_2 = make_customer_record_two("Mike")
    customer_3 = make_customer_record_two("Meredith")
    print(customer_1, customer_2, customer_3)


# Run 2 times passing in different parameters
# parameters accessed using request.param
@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
    smtp_connection.close()

# mark the 3rd arg to skip or fail
@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.xfail), pytest.param(3, marks=pytest.mark.skip)])
def data_set(request):
    return request.param

def test_data(data_set):
    assert data_set < 2