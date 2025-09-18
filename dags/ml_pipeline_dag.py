from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {"owner": "airflow", "retries": 1}

with DAG(
    dag_id="ml_pipeline_docker",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extract = DockerOperator(
        task_id="extract",
        image="extract:latest",
        command="python extract.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    upload_s3 = DockerOperator(
        task_id="upload_s3",
        image="upload_s3:latest",
        command="python upload_s3.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    transform = DockerOperator(
        task_id="transform",
        image="transform:latest",
        command="python transform.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    train = DockerOperator(
        task_id="train",
        image="train:latest",
        command="python train.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    evaluate = DockerOperator(
        task_id="evaluate",
        image="evaluate:latest",
        command="python evaluate.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    save_parquet = DockerOperator(
        task_id="save_parquet",
        image="save_parquet:latest",
        command="python save_parquet.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=["/tmp/data:/app/data"],
    )

    extract >> upload_s3 >> transform >> train >> evaluate >> save_parquet
