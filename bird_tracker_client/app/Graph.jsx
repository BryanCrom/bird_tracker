import {StyleSheet, View} from "react-native";
import { BarChart } from "react-native-gifted-charts";
import {useEffect, useState} from "react";

const Graph = () => {

    const data = [ {value: 10}, {value: 10}, {value: 10}, {value: 10}, {value: 10}, {value: 10},  {value: 10} ]

    const [chartData, setChartData] = useState([]);
    const [currentDate, setCurrentDate] = useState(new Date());
    const [currentEndDate, setCurrentEndDate] = useState(new Date());
    const [bird, setBird] = useState("all");

    useEffect(() => {
        const fetchData = async () => {

            const { endDate, startDate } = getWeekRange(currentDate);
            setCurrentEndDate(new Date(endDate));

        }
    },[])

    const fetchWeeklyData = async (startDate, endDate, bird) => {

        try{

        }catch(e) {
            console.log(e)
        }
    }

    const getWeekRange = (date) => {
        const startOfWeek = new Date(date.setDate(new Date().getDate() - date.getDay()));
        const endOfWeek = new Date(date.setDate(startOfWeek.getDate() + 6));

        return {
            startOfWeek: Math.floor(startOfWeek.getTime()),
            endOfWeek: Math.floor(endOfWeek.getTime()),
        }
    }

    return (
        <View style={styles.container}>
            <BarChart
                data={chartData}
                width={290}
                height={250}
                barWidth={20}
                barBorderRadius={3}
                gradientColor={"green"}
                showGradient={true}
                spacing={20}
                xAxisThickness={0}
                yAxisThickness={0}
                isAnimated={true}
            />
        </View>
    );
}

export default Graph;

const styles = StyleSheet.create({
    container: {
        margin: 20,
    },
})