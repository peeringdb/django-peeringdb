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

