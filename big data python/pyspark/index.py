import os
import findspark

# Configurar las variables de entorno
os.environ["SPARK_HOME"] = "C:/pySpark/spark"
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-17"

# Inicializar findspark
findspark.init()

from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder.appName("ExampleApp").master("local[*]").getOrCreate()

# Crear un DataFrame simple
data = [{"Saludar": "Wake up, pay attention"} for x in range(10)]
df = spark.createDataFrame(data)

# Mostrar el DataFrame
df.show()

# Personalizar la sesión de Spark
spark = SparkSession.builder.master("local[*]").appName("MiApp").getOrCreate()
sc = spark.sparkContext
