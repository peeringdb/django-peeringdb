# Synchronizing your database from peeringdb

## Install the PeeringDB Client

To synchronize your databases from production peeringdb, you will need to install the peeringdb client.

If you are using a virtualenv, it's probably most convenient to do this in the same virtualenv that you use to run your django instace that has django-peeringdb installed.

```sh
pip install peeringdb
```

## Configure the PeeringDB Client

Run the following command to start the configuration process of the peeringdb client.

We want to point it at the same database that you use for your django instance.

```sh
peeringdb config set
```

Most settings can be used with their default values, but the `orm.database` keys are the ones you will want to specify correctly.

After the config is written you may also edit by hand in `~/.peeringdb/config.yaml`


## Sync data

Once configured, run the `sync` command to sync to your database.

```
peeringdb sync
```

## Common problems

### `status="ok"` no longer returns every active connection

A netixlan that is active but not currently passing traffic now carries
`status="not-operational"` instead of `status="ok"` with `operational=False`
(#1742). Once migration `0042` has run against your local database, queries
that filter on `status="ok"` silently stop returning those connections.

Filter on the full set of live statuses instead:

```python
NetworkIXLan.objects.filter(status__in=["ok", "not-operational"])
```

Soft-delete filtering needs no change: handleref's `undeleted()` excludes only
`status="deleted"`, so it keeps returning non-operational connections. (Note
that the default manager does not filter by status at all -- `undeleted()` is
an explicit opt-in.) `status` is a plain `CharField` with no `choices`, so the
new value needs no schema change on your side -- it does not want a choice
list adding to it.

