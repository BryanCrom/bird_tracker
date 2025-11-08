import {StyleSheet, View} from "react-native";
import { BarChart } from "react-native-gifted-charts";
import {useEffect, useState} from "react";
import SegmentedControl from "@react-native-segmented-control/segmented-control";
import { API_URL } from '@env';




const Graph = () => {

    const data = [ {value: 10}, {value: 10}, {value: 10}, {value: 10}, {value: 10}, {value: 10},  {value: 10} ]

    const [chartData, setChartData] = useState([]);
    const [currentDate, setCurrentDate] = useState(new Date());
    const [currentEndDate, setCurrentEndDate] = useState(new Date());
    const [bird, setBird] = useState("all");
    const [selectedIndex, setSelectedIndex] = useState(0);
    const [chartKey, setChartKey] = useState(0);

    const segments = ["all", "fantail", "tui", "kiwi", "kaka"]

    useEffect(() => {
        const fetchData = async () => {
            try {
                const {endDate, startDate} = getWeekRange(currentDate);
                setCurrentEndDate(new Date(endDate));
                const response = await fetch(`${API_URL}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        startDate: startDate,
                        endDate: endDate,
                        location: "The Auckland Botanical Gardens",
                        bird: bird
                    })
                })

                const data = await response.json();

                setChartData(processData(data))
            }
            catch (error) {
                console.log(error);
            }
        }

        void fetchData()
    },[chartKey, selectedIndex]);

    const processData = (data) => {
        const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

        let barData = days.map((label) => ({
            label,
            value: 0,
        }))

        data.forEach((item) => {
            const dayIndex = item.day;

            if (dayIndex >= 0 && dayIndex < 7) {
                barData[dayIndex].value = item.count;
            }
        })

        return barData;
    }

    const getWeekRange = (date) => {
        // Always work with a copy so we don’t mutate the original
        const current = new Date(date);

        const day = current.getDay(); // Sunday = 0
        const startOfWeek = new Date(current);
        startOfWeek.setDate(current.getDate() - day);
        startOfWeek.setHours(0, 0, 0, 0);

        const endOfWeek = new Date(startOfWeek);
        endOfWeek.setDate(startOfWeek.getDate() + 6);
        endOfWeek.setHours(23, 59, 59, 999);

        return {
            startDate: startOfWeek.getTime(), // milliseconds since epoch
            endDate: endOfWeek.getTime(),
        };
    };

    return (
        <View style={styles.container}>
            <BarChart
                key={chartKey}
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
            <SegmentedControl
                values={segments}
                selectedIndex={selectedIndex}
                onChange={(event) => {
                    const index = event.nativeEvent.selectedSegmentIndex
                    setSelectedIndex(index);
                    setBird(segments[index]);
                }}
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