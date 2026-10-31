# slugkit

Turn any text into clean, URL-safe slugs, with Unicode folding and unique-slug helpers.

## Usage

```python
from slugkit import slugify, unique_slug

slugify("Crème Brûlée & Friends!")      # -> "creme-brulee-friends"
unique_slug("hello", {"hello", "hello-2"})  # -> "hello-3"
```

## Test

```bash
pip install pytest && pytest
```

## License

MIT
