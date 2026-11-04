"""Day 01: names, values and Python built-in types."""

service_name = "document-assistant"
max_retries = 3
request_timeout_seconds = 12.5
is_enabled = True
optional_model = None

settings = {
    "service_name": service_name,
    "max_retries": max_retries,
    "request_timeout_seconds": request_timeout_seconds,
    "is_enabled": is_enabled,
    "optional_model": optional_model,
}

for name, value in settings.items():
    print(f"{name} = {value!r}; type = {type(value).__name__}")

print("max_retries is an int:", isinstance(max_retries, int))
print("True is an int:", isinstance(True, int))
