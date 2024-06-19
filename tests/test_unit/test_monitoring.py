import os
from unittest.mock import patch

import pandas as pd
from pytest import mark
from sqlalchemy import create_engine

from dags.config import MONITORING_TABLE_NAME
from formation_indus_ds_avancee.monitoring import monitor_with_io


@patch('pandas.read_csv')
def test_monitor_with_io_should_write_predictions_mean_to_db(mocked_read_csv):
    # Given
    predictions_folder = 'test_pred_folder'
    given_date = pd.to_datetime('20200101-120000', format='%Y%m%d-%H%M%S')
    predictions = pd.DataFrame({'predictions_time': [given_date, given_date],
                                'predictions': [12, 14]})
    mocked_read_csv.return_value = predictions
    db_con_str = 'sqlite:///test_db.db'
    # Start filling expected
    expected = pd.DataFrame(
        {"Datetime": "2024-06-19T11:00:00+01:00",
         "Mean": 12.4,
         }, index=[0])
    # End filling expected

    # When
    monitor_with_io(predictions_folder, db_con_str, monitoring_table_name=MONITORING_TABLE_NAME)
    engine = create_engine(db_con_str)
    db_conn = engine.connect()
    actual = pd.read_sql(f'SELECT * FROM {MONITORING_TABLE_NAME}', db_conn, parse_dates=['predictions_time'])

    # Then
    pd.testing.assert_frame_equal(expected, actual)
    db_conn.close()
    os.remove('test_db.db')


def test_monitoring_table_name_as_been_changed():
    # Please change monitoring table name so that you don't overwrite monitoring from other attendees
    assert MONITORING_TABLE_NAME != "monitoring"
