echo "started building binary"
time env/bin/python -m nuitka --onefile \
                         --include-module=sqlalchemy.sql.default_comparator \
                         --include-data-files=data_dir/ml_model.txt=data_dir/ \
                         --include-data-files=data_dir/sample_license=data_dir/ \
                         --include-module=sqlalchemy.dialects \
                         --linux-onefile-icon=data_dir/python3.xpm \
                         sample_binary.py
echo "finished building binary"
