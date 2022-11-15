import { useAppSelector } from "../../hook/redux"
import { Button, Table } from "antd"
import Navigation from "../Navigetion/Navigation"
import { useAppDispatch } from "../../hook/redux"
import axios from "axios"
import { mainSlice } from "../../store/reducers/MainSlice"

function ResultPage() {
  const { allFiles, selectAllFileResult } = useAppSelector(
    (state) => state.mainReducer
  )
  const dispatch = useAppDispatch()
  const { setAllFile } = mainSlice.actions

  let columns = []
  let data = []

  for (let i in allFiles[0].result) {
    columns.push({ title: i, dataIndex: i })
  }

  for (let i of allFiles) {
    for (let j of selectAllFileResult) {
      if (i.id === j) {
        data.push(i.result)
      }
    }
  }

  return (
    <div className="h-[100vh] w-full overflow-y-auto">
      <div className="w-full h-[56px] flex justify-start items-center">
        <Navigation />
        <p className="ml-[50px] text-[20px]">Результат</p>
        <Button
          type="primary"
          className="bg-black ml-[100px]"
          onClick={() => {
            axios
              .post(
                "http://127.0.0.1:8000/export_to_excel",
                selectAllFileResult
              )
              .then(res => console.log(res.data))
              .catch(err => console.log(err))
          }}
        >
          Экспорт
        </Button>
      </div>
      <div>
        <Table columns={columns.reverse()} dataSource={data.reverse()} />
      </div>
    </div>
  )
}

export default ResultPage
