#!/bin/sh

until who | grep "$1" > /dev/null; do
  sleep 60
done

# Now ring the bell and anounce the expected user

echo -e '\a'
echo "******** $1 has just logged in ********"
exit 0

