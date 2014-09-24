# django-auth-abakus
A django auth module that can be used to to authenticate users against
the API of abakus.no. If you would like to use it you need a API token.
Contact webkom@abakus.no to request one.

## Usage
Set the authentication backend to *AbakusBackend*

```python
    AUTHENTICATION_BACKENDS = ( 'abakus.auth.AbakusBackend', )
```

The token should be added in the django-settings as `ABAKUS_TOKEN`.


## Contribute
Open an issue or a pull-request with your fix or awesome new feature.
Make sure to check those that are already open, to avoid duplicates.

--------
MIT © webkom, Abakus Linjeforening
