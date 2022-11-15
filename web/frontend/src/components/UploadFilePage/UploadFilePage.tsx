import React, { useState } from "react"
import Navigation from "../Navigetion/Navigation"
import { Button } from "antd"
import { Link } from "react-router-dom"
import axios from "axios"
import { useAppDispatch, useAppSelector } from "../../hook/redux"
import { mainSlice } from "../../store/reducers/MainSlice"
import UploadFileList from "./UploadFileList/UploadFileList"

import { List } from "antd"

function UploadFilePage() {
  const dispatch = useAppDispatch()

  const data: any[] = []

  const [flag, setArrayUploadFile] = useState(false)
  const { allFiles, selectAllFileResult } = useAppSelector(
    (state) => state.mainReducer
  )

  const { setAllFile } = mainSlice.actions
  const { setAllFileSelect } = mainSlice.actions

  let socket = new WebSocket("ws:/localhost:8000/ws")

  socket.onopen = function (e) {
    console.log("[open] Соединение установлено")
    console.log("Отправляем данные на сервер")
    // socket.send('Меня зовут Джон')
  }

  socket.onmessage = function (event) {
    setArrayUploadFile(event.data)
    axios
      .post("http://127.0.0.1:8000/send_gpzu", JSON.parse(event.data))
      .then((res) => {
        console.log(res.data)
        let array = res.data.map((el: number) => el)
        console.log(array)
        dispatch(setAllFileSelect(array))
      })
      .then(() => {
        axios
          .get(`http://127.0.0.1:8000/get_all_gpzu`)
          .then((data) => {
            dispatch(setAllFile(data.data))
          })
          .catch((err) => console.log(err))
      })
      .catch((err) => console.log(err))

    console.log(`[message] Данные получены с сервера: ${event.data}`)
  }

  socket.onclose = function (event) {
    if (event.wasClean) {
      console.log(
        `[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`
      )
    } else {
      // например, сервер убил процесс или сеть недоступна
      // обычно в этом случае event.code 1006
      console.log("[close] Соединение прервано")
    }
  }

  socket.onerror = function (error) {
    console.log(`[error]`)
  }

  return (
    <div className="h-[100vh] w-full">
      <div className="w-full h-[56px] flex justify-start items-center border-b-[1px] border-black">
        <Navigation />
        <p className="ml-[50px] text-[20px]">Загрузка файлов</p>
        <Button
          className="ml-[20px] text-black border-black"
          type="primary"
          onClick={(event) => {
            console.log(1)
            socket.send(JSON.stringify({ type: "open_file_manager" }))
          }}
        >
          Загрузить файлы
        </Button>
        <Link to="/result/">
          <Button className="ml-[20px]  text-black border-black" type="primary">
            Результат
          </Button>
        </Link>
      </div>
      <div className="ml-[50px] mt-[20px] w-full h-auto flex flex-column">
        <UploadFileList />
      </div>
    </div>
  )
}

export default UploadFilePage
