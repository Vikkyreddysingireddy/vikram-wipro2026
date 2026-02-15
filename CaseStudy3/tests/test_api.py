import requests

def test_add_patient(base_url, patient_data):
    res = requests.post(f"{base_url}/api/patients", json=patient_data)
    assert res.status_code == 201
    assert res.json()["name"] == patient_data["name"]

def test_get_patients(base_url):
    res = requests.get(f"{base_url}/api/patients")
    assert res.status_code == 200
