#!/bin/bash

# Start SQL Server
echo "======= MSSQL SERVER STARTING ========" 
echo "Environment list"
echo SA_PASSWORD=$SA_PASSWORD
echo MSSQL_USER=$MSSQL_USER
echo MSSQL_PASSWORD=$MSSQL_PASSWORD
echo MSSQL_DB=$MSSQL_DB

/opt/mssql/bin/sqlservr &

# wait for MSSQL server to start
export STATUS=1
i=0

echo "======= WAIT FOR MSSQL SERVER ========"

while [[ $STATUS -ne 0 ]] && [[ $i -lt 30 ]]; do
        i=$i+1
        /opt/mssql-tools/bin/sqlcmd -t 1 -U sa -P $SA_PASSWORD -Q "select 1" >> /dev/null
        STATUS=$?
done

if [ $STATUS -ne 0 ]; then
        echo "Error: MSSQL SERVER took more than thirty seconds to start up."
        exit 1
fi

echo "======= MSSQL SERVER STARTED ========" | tee -a /var/opt/mssql/log/config.log
# Run the setup script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i /tmp/setup.sql

echo "======= MSSQL CONFIG COMPLETE =======" | tee -a /var/opt/mssql/log/config.log

tail -f /dev/null
