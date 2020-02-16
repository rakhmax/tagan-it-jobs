#!/bin/bash

echo -n "Enter database user: "
read user

mysql -u $user -p < ./db.sql