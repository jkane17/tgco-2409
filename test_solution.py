
import requests
from solution import get_data, validate, get_max_amount, get_customers_amounts
from unittest import TestCase
import pandas as pd

class TestGetData(TestCase):
    def test_ok(self):
        url = "http://localhost:9090/"
        data = get_data(url)
        self.assertIsNotNone(data)

    def test_timeout(self):
        url = "http://localhost:9091/"
        self.assertRaises(requests.exceptions.Timeout, get_data, url)

class TestValidate(TestCase):
    def setUp(self):
        self.customers_df = [
            {
                "ID": 0,
                "name": "Alice",
                "surname": "Klark"
            },
            {
                "ID": 1,
                "name": "Bob",
                "surname": "McAdoo"
            },
        ]

        self.non_unique_customers_df = [
            {
                "ID": 0,
                "name": "Alice",
                "surname": "Klark"
            },
            {
                "ID": 0,
                "name": "Bob",
                "surname": "McAdoo"
            },
        ]

    def test_unique_ids(self):
        try:
            validate(self.customers_df)
        except ValueError:
            self.fail()

    def test_non_unique_ids(self):
        self.assertRaises(ValueError, validate, self.non_unique_customers_df)

class TestGetMaxAmount(TestCase):
    def setUp(self):
        self.invoices_df = pd.DataFrame([
            {
                "ID": 0,
                "customerId": 0,
                "amount": 12
            },
            {
                "ID": 1,
                "customerId": 0,
                "amount": 235.78
            },
            {
                "ID": 2,
                "customerId": 1,
                "amount": 5.06
            },
        ])
        self.mulit_invoices_df = pd.DataFrame([
            {
                "ID": 0,
                "customerId": 0,
                "amount": 12
            },
            {
                "ID": 1,
                "customerId": 1,
                "amount": 12
            }
        ])

    def test_returns_df(self):
        res = get_max_amount(self.invoices_df)
        self.assertIsInstance(res, pd.DataFrame)

    def test_correct_amount(self):
        amount = get_max_amount(self.invoices_df).iloc[0]["amount"]
        self.assertEqual(247.78, amount)

    def test_multi_max_amounts(self):
        num_rows = len(get_max_amount(self.mulit_invoices_df))
        self.assertEqual(2, num_rows)

class TestGetCustomersAmounts(TestCase):
    def setUp(self):
        self.customers_df = pd.DataFrame([
            {
                "ID": 0,
                "name": "Alice",
                "surname": "Klark"
            },
            {
                "ID": 1,
                "name": "Bob",
                "surname": "McAdoo"
            },
        ])
        self.max_amount_df = pd.DataFrame([
            {
                "ID": 0,
                "customerId": 0,
                "amount": 12
            },
        ])
        self.multi_max_amount_df = pd.DataFrame([
            {
                "ID": 0,
                "customerId": 0,
                "amount": 12
            },
            {
                "ID": 1,
                "customerId": 1,
                "amount": 12
            },
        ])

    def test_correct_columns(self):
        res = get_customers_amounts(self.customers_df, self.max_amount_df)
        self.assertListEqual(list(res.columns), ["name", "surname", "amount"])

    def test_correct_values(self):
        res = get_customers_amounts(self.customers_df, self.max_amount_df)
        self.assertEqual(res["name"][0], "Alice")
        self.assertEqual(res["surname"][0], "Klark")
        self.assertEqual(res["amount"][0], 12)

    def test_multi_correct_values(self):
        res = get_customers_amounts(self.customers_df, self.multi_max_amount_df)
        self.assertEqual(res["name"][0], "Alice")
        self.assertEqual(res["surname"][0], "Klark")
        self.assertEqual(res["amount"][0], 12)
        self.assertEqual(res["name"][1], "Bob")
        self.assertEqual(res["surname"][1], "McAdoo")
        self.assertEqual(res["amount"][1], 12)
