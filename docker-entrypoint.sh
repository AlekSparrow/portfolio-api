#!/usr/bin/env sh

echo Run django migrations
python manage.py migrate || exit 0
echo Collect staticfiles
python manage.py collectstatic --noinput --clear || exit 0

echo Creating django superuser
if [ -n "$ADMIN_USER" ] && [ -n "$ADMIN_PASSWD" ] ; then
    (python manage.py createsuperuser --no-input; exit 0)
fi

exec "$@"
