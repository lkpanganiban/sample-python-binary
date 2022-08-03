echo "started building binary"
time env/bin/python -m nuitka --onefile \
                         --include-module=sqlalchemy.sql.default_comparator \
                         --include-data-files=data_dir/*=data_dir/ \
                         --include-module=sqlalchemy.dialects \
                         sample_binary.py
echo "finished building binary"
